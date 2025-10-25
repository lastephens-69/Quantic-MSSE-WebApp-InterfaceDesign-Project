# 5–10 minute Demo Script (Checklist)

1) **Intro & ID**
   - Show your government ID; state your name and project title.

2) **App Overview**
   - Show navigation among: Home, Menu, Reservations, About Us, Gallery.

3) **Newsletter Signup (Home)**
   - Enter name/email; submit; show success message.
   - (Optional) Show DB row in `customers` with `newsletter_signup=true`.

4) **Reservations**
   - Book a table: choose date/time, guests, name, email; submit.
   - Show confirmation w/ assigned table number.
   - Create several reservations for the same time to prove unique table assignment.
   - Attempt >30 bookings for one timeslot to trigger “fully booked” message.

5) **Menu / About / Gallery**
   - Briefly highlight design, responsiveness (resize window / Chrome device toolbar).
   - Point out Flexbox and Grid usage.

6) **Back‑end State**
   - Hit `GET /api/reservations` filtered by the chosen time.
   - Optionally psql into DB to show `customers` and `reservations` tables.

7) **Implementation Notes**
   - React + Vite + Router, CSS Flexbox/Grid.
   - Flask API + SQLAlchemy + PostgreSQL.
   - Discuss AI assistance: scaffolding, forms, endpoints, README.

8) **Close**
   - Summarize how requirements were met; thank the viewer.
