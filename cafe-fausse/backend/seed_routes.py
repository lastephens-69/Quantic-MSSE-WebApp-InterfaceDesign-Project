# seed_routes.py
"""
Admin seeding routes for Café Fausse (staging only)
Creates demo customers and reservations for the next week.
Requires header:  X-Admin-Token: <ADMIN_TOKEN>
"""

import os
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo
from flask import request, jsonify
from sqlalchemy import text
from models import Customer, Reservation
from database import SessionLocal  # adjust import if using Flask-SQLAlchemy

# --- Config ---
CHICAGO_TZ = ZoneInfo("America/Chicago")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "dev-secret-123")
MAX_PER_SLOT = 30


# --- Helpers ---
def _ensure_demo_customers(session):
    """Create demo customers if missing and return the list."""
    demo_data = [
        ("Avery Chen", "avery.chen@example.com", "202-555-0101", True),
        ("Jordan Patel", "jordan.patel@example.com", "202-555-0102", False),
        ("Riley Nguyen", "riley.nguyen@example.com", "202-555-0103", True),
        ("Samira Ali", "samira.ali@example.com", "202-555-0104", False),
        ("Diego Romero", "diego.romero@example.com", "202-555-0105", False),
        ("Priya Shah", "priya.shah@example.com", "202-555-0106", True),
        ("Maya Thompson", "maya.thompson@example.com", "202-555-0107", True),
        ("Ethan Rivera", "ethan.rivera@example.com", "202-555-0108", False),
        ("Zoe Park", "zoe.park@example.com", "202-555-0109", True),
        ("Leo Carter", "leo.carter@example.com", "202-555-0110", False),
    ]
    existing_emails = {e for (e,) in session.query(Customer.email).filter(Customer.email.like("%@example.com"))}
    to_add = [
        Customer(name=n, email=e, phone=p, newsletter_signup=ns)
        for (n, e, p, ns) in demo_data
        if e not in existing_emails
    ]
    if to_add:
        session.add_all(to_add)
        session.flush()
    return session.query(Customer).filter(Customer.email.like("%@example.com")).order_by(Customer.id).all()


def _seed_reservations(session, days=7):
    """Create demo reservations for the next week with varied loads."""
    customers = _ensure_demo_customers(session)
    if not customers:
        return {"created_slots": 0, "created_reservations": 0}

    pattern = [2, 4, 3, 5, 2, 6]
    slot_times = [time(12, 0), time(18, 30), time(19, 0), time(19, 30)]
    today = datetime.now(CHICAGO_TZ).date()
    full_day_idx, full_slot_time = min(4, days - 1), time(19, 0)

    created_slots = created_res = 0
    total_customers = len(customers)

    for d in range(days):
        day = today + timedelta(days=d)
        for slot in slot_times:
            dt = datetime.combine(day, slot, tzinfo=CHICAGO_TZ)
            target = (
                MAX_PER_SLOT if (d == full_day_idx and slot == full_slot_time)
                else (8 if slot == time(12, 0) else 12 if slot == time(18, 30)
                      else 18 if slot == time(19, 0) else 14)
            )
            for n in range(1, target + 1):
                if session.query(Reservation.id).filter_by(time_slot=dt, table_number=n).first():
                    continue
                c = customers[(n - 1) % total_customers]
                session.add(
                    Reservation(
                        customer_id=c.id,
                        party_size=pattern[(n - 1) % len(pattern)],
                        time_slot=dt,
                        table_number=n,
                    )
                )
                created_res += 1
            created_slots += 1
    return {"created_slots": created_slots, "created_reservations": created_res}


# --- Main route registration ---
def register_seed_routes(app):
    """Attach admin seeding routes to the Flask app."""

    @app.post("/admin/seed")
    def admin_seed():
        token = request.headers.get("X-Admin-Token")
        if token != ADMIN_TOKEN:
            return jsonify({"error": "unauthorized"}), 401

        days = int(request.args.get("days", 7))
        wipe_customers = request.args.get("wipe_customers", "false").lower() == "true"

        session = SessionLocal()
        try:
            # Truncate old data
            session.execute(text("TRUNCATE TABLE reservations RESTART IDENTITY CASCADE;"))
            if wipe_customers:
                session.execute(text("TRUNCATE TABLE customers RESTART IDENTITY CASCADE;"))
            session.commit()

            # Reseed
            result = _seed_reservations(session, days=days)
            session.commit()
            return jsonify({"ok": True, "wiped_customers": wipe_customers, **result}), 200
        except Exception as e:
            session.rollback()
            return jsonify({"ok": False, "error": str(e)}), 500
        finally:
            session.close()
