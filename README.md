# Café Fausse — Web Application & Interface Design (Quantic MSSE Project #2)

**Course:** MSEE – Web Application and Interface Design  
**Student:** LaDonna Stephens  
**Project:** Café Fausse Restaurant Website  
**Framework:** Framework: React (Vite) + Flask (Python) + PostgreSQL (backend)  
**Date:** October 2025  

---

## 🌟 Overview

Café Fausse is a modern fine-dining restaurant website built for the Quantic MSSE Project #2 assignment.  
The application demonstrates full-stack design principles, user-friendly UI components, and clean, modular code.

The site reflects **Café Fausse’s mission**: blending traditional Italian flavors with modern culinary innovation.  
Founded in 2010 by **Chef Antonio Rossi** and **restaurateur Maria Lopez**, the restaurant’s goal is to deliver an unforgettable dining experience rooted in both **quality** and **creativity**.

---

## 🧭 Features & Functional Requirements

| ID | Requirement | Implementation |
|----|--------------|----------------|
| **FR-01** | Homepage introduction | Hero section with image, tagline, and CTA button “Reserve a Table.” |
| **FR-02** | Menu display | Stacked, centered menu with Bilbo Swash Caps typography and images for each dish. |
| **FR-03** | Reservation form | Functional reservation form (React form + backend route to save entries). |
| **FR-04** | Newsletter subscription | Newsletter section with name, email, and phone fields (API call + validation). |
| **FR-05** | Responsive design | Fully responsive using flex/grid layouts and media queries. |
| **FR-06** | Navigation bar | Sticky black header with gold accent, brand logo text, and page links. |
| **FR-07** | Footer | Matching black footer with gold accent and contact details. |
| **FR-08** | Gallery | Filterable gallery with categories (Dishes, Catering, Location, Behind the Scenes). |
| **FR-09** | Contact/Location | Address displayed on Home and Footer: **1234 Culinary Ave, Suite 100, Washington, DC 20002** |
| **FR-10** | About page history | Includes founding date, founders’ names, mission statement, and restaurant history. |
| **FR-11** | Founder biographies & commitment | Detailed bios for Maria Lopez and Antonio Rossi, plus “Our Commitment” section. |

---

## 🗂️ File Structure

frontend/
├── src/
│ ├── assets/
│ │ └── cafe/
│ │ ├── Dishes/
│ │ ├── Catering/
│ │ ├── Location/
│ │ └── Behind The Scenes/
│ ├── components/
│ │ ├── NavBar.jsx
│ │ ├── Footer.jsx
│ │ └── ...
│ ├── pages/
│ │ ├── Home.jsx / Home.css
│ │ ├── Menu.jsx / Menu.css
│ │ ├── Gallery.jsx / Gallery.css
│ │ ├── Reservations.jsx / Reservations.css
│ │ └── About.jsx / About.css
│ ├── services/
│ │ └── api.js
│ └── main.jsx
backend/
├── app.js
├── routes/
└── db/
README.md

---

## 🎨 Design Choices

- **Typography:**  
  - *Bilbo Swash Caps* for headings & titles  
  - *Lora* for body text  
- **Color Palette:**  
  - Black (`#000`) background header/footer  
  - Muted Gold (`#bfa14a`) accent  
  - Warm ivory/white backgrounds for content sections  
- **UI Consistency:**  
  - Gold accent for active navigation and buttons  
  - Rounded corners and soft shadows for card elements  
  - Gallery and menu use consistent image aspect ratios  

---

## ⚙️ Running the Project Locally

### 1. Clone or unzip the repository
```bash
git clone https://github.com/<your-username>/cafe-fausse.git
cd cafe-fausse

cd backend
.\.venv\scripts\activate
pip install -r requirements.txt
python app.py

cd ../frontend
npm install
npm run dev

Access the site at http://localhost:5173


---
## 📸 Image Credits
Images were created or curated using Canva Pro.
They were organized into subfolders for clear categorization:
Dishes/ – menu items
Catering/ – behind-the-scenes service
Location/ – restaurant interiors/exteriors
Behind The Scenes/ – team and event photos

---
## 💬 Notes for Evaluation

The design meets all functional requirements (FR-01 → FR-11).

Newsletter and Reservation forms are connected to API endpoints and validate user input.

Gallery auto-groups and filters images by folder.

Fully responsive and tested across desktop, tablet, and mobile.

Code is modular and readable with consistent naming conventions.

---
🧑‍🍳 Acknowledgments

Created by LaDonna Stephens for the Quantic School of Business and Technology
Master of Science in Software Engineering – Web Application and Interface Design


