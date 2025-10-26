import os, random, datetime as dt
from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import select, and_
from dotenv import load_dotenv
from database import Base, engine, get_db
from models import Customer, Reservation
from sqlalchemy.orm import Session

load_dotenv()

app = Flask(__name__)
NETLIFY_URL = https://cafe-fausse.netlify.app"
allowed_origins = [NETLIFY_URL] if NETLIFY_URL else []
CORS(app, resources={r"/api/*": {
    "origins": allowed_origins,
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type"],
    "max_age": 86400
}})
# Initialize tables if they don't exist
Base.metadata.create_all(bind=engine)

def parse_iso_datetime(value: str) -> dt.datetime:
    # Accepts ISO strings like "2025-10-31T19:30:00"
    try:
        # Allow timezone-less -> assume local; convert to naive for consistent storage or use UTC
        return dt.datetime.fromisoformat(value)
    except Exception:
        raise ValueError("Invalid datetime format. Use ISO 8601, e.g., 2025-10-31T19:30:00")

@app.get("/api/health")
def health():
    return jsonify({"ok": True}), 200

@app.post("/api/newsletter")
def newsletter():
    payload = request.get_json(force=True)
    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip().lower()
    phone = (payload.get("phone") or "").strip() or None

    if not name or not email or "@" not in email:
        return jsonify({"error": "Name and valid email are required"}), 400

    with Session(engine) as db:
        # Upsert by email
        customer = db.scalar(select(Customer).where(Customer.email == email))
        if customer:
            customer.name = name or customer.name
            customer.phone = phone if phone is not None else customer.phone
            customer.newsletter_signup = True
        else:
            customer = Customer(name=name, email=email, phone=phone, newsletter_signup=True)
            db.add(customer)
        db.commit()
    return jsonify({"status": "subscribed"}), 201

@app.post("/api/reservations")
def create_reservation():
    payload = request.get_json(force=True)
    try:
        time_slot_str = payload.get("time_slot")
        time_slot = parse_iso_datetime(time_slot_str)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    guests = int(payload.get("guests") or 0)
    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip().lower()
    phone = (payload.get("phone") or "").strip() or None

    if guests <= 0 or not name or not email or "@" not in email:
        return jsonify({"error": "Guests must be > 0, and name/email are required"}), 400

    total_tables = 30

    with Session(engine) as db:
        # ensure customer exists (upsert)
        customer = db.scalar(select(Customer).where(Customer.email == email))
        if not customer:
            customer = Customer(name=name, email=email, phone=phone, newsletter_signup=False)
            db.add(customer)
            db.flush()  # get id

        # Find taken tables for the exact time_slot
        taken = db.scalars(select(Reservation.table_number).where(Reservation.time_slot == time_slot)).all()
        taken_set = set(taken)

        if len(taken_set) >= total_tables:
            return jsonify({"error": "Time slot fully booked. Please choose another time."}), 409

        # Choose a random free table
        free_tables = [t for t in range(1, total_tables + 1) if t not in taken_set]
        table_number = random.choice(free_tables)

        reservation = Reservation(customer_id=customer.id, time_slot=time_slot, table_number=table_number)
        db.add(reservation)
        db.commit()

        return jsonify({
            "status": "confirmed",
            "reservation": {
                "id": reservation.id,
                "customer_id": customer.id,
                "time_slot": time_slot.isoformat(),
                "table_number": table_number
            }
        }), 201

@app.get("/api/reservations")
def list_reservations():
    # Simple admin-ish endpoint to view reservations (optional convenience)
    time_slot_str = request.args.get("time_slot")
    with Session(engine) as db:
        query = select(Reservation)
        if time_slot_str:
            try:
                ts = parse_iso_datetime(time_slot_str)
                query = query.where(Reservation.time_slot == ts)
            except Exception:
                return jsonify({"error": "Invalid time_slot query param"}), 400
        rows = db.scalars(query).all()
        data = [{
            "id": r.id,
            "customer_id": r.customer_id,
            "time_slot": r.time_slot.isoformat(),
            "table_number": r.table_number
        } for r in rows]
        return jsonify(data), 200

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    app.run(host=host, port=port)
