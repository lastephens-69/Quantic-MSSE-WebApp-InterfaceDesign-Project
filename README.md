# ☕ Café Fausse — Web Application & Interface Design (Quantic MSSE Project #2)

**Course:** MSEE – Web Application and Interface Design  
**Student:** LaDonna Stephens  
**Project:** Café Fausse Restaurant Website  
**Framework:** React (Vite) + Flask (Python) + PostgreSQL  
**Date:** October 2025  

---

## 🌟 Overview

Café Fausse is a modern fine-dining restaurant website built for the **Quantic MSSE Project #2** assignment.  
The application demonstrates full-stack design principles, user-friendly UI components, and clean, modular code.

The site reflects **Café Fausse’s mission**: blending traditional Italian flavors with modern culinary innovation.  
Founded in 2010 by **Chef Antonio Rossi** and **restaurateur Maria Lopez**, the restaurant’s goal is to deliver an unforgettable dining experience rooted in both **quality** and **creativity**.

---

## 🧭 Features & Functional Requirements

| ID | Requirement | Implementation |
|----|--------------|----------------|
| **FR-01** | Homepage introduction | Hero section with image, tagline, and CTA button “Reserve a Table.” |
| **FR-02** | Menu display | Stacked, centered menu with *Bilbo Swash Caps* typography and images for each dish. |
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

### Frontend (`/frontend`)
```
frontend/
├── public/
│   └── _redirects
├── src/
│   ├── assets/
│   │   └── cafe/
│   │       ├── Behind the Scenes/
│   │       ├── Catering/
│   │       ├── Dishes/
│   │       ├── founders/
│   │       └── Location/
│   ├── components/
│   │   ├── footer.css
│   │   ├── Footer.jsx
│   │   └── NavBar.jsx
│   ├── pages/
│   │   ├── about.css / About.jsx
│   │   ├── admin.css / Admin.jsx
│   │   ├── gallery.css / Gallery.jsx
│   │   ├── home.css / Home.jsx
│   │   ├── menu.css / Menu.jsx
│   │   └── Reservations.jsx
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   ├── main.jsx
│   ├── styles.css
│   └── vite.config.js
├── package.json
├── package-lock.json
└── index.html
```

### Backend (`/backend`)
```
backend/
├── .env
├── .env.sample
├── app.py
├── database.py
├── models.py
├── requirements.txt
├── schema.sql
└── package-lock.json
```

---

## 🎨 Design Choices

**Typography**
- *Bilbo Swash Caps* for headings & titles  
- *Lora* for body text  

**Color Palette**
- Black (`#000`) background header/footer  
- Muted Gold (`#bfa14a`) accent  
- Warm ivory/white backgrounds for content sections  

**UI Consistency**
- Gold accent for active navigation and buttons  
- Rounded corners and soft shadows for card elements  
- Gallery and menu use consistent image aspect ratios  

---

## ⚙️ Running the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/lastephens-69/Quantic-MSSE-WebApp-InterfaceDesign-Project.git
cd Quantic-MSSE-WebApp-InterfaceDesign-Project
```

### 2️⃣ Create environment files
Copy the provided `.env.sample` files into `.env`.

**Windows PowerShell**
```powershell
Copy-Item backend\.env.sample backend\.env
Copy-Item frontend\.env.sample frontend\.env
```

**macOS/Linux**
```bash
cp backend/.env.sample backend/.env
cp frontend/.env.sample frontend/.env
```

### 3️⃣ Backend Setup
```bash
cd backend
python -m venv .venv
# Activate the environment
.\.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
python app.py
```

Backend runs on → **http://127.0.0.1:5000**

### 4️⃣ Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend runs on → **http://localhost:5173**

The `vite.config.js` includes a proxy for `/api/*` → `http://127.0.0.1:5000` for seamless integration.

---

## 🌐 Staging / Demo Sites

| Component | Platform | URL |
|------------|-----------|-----------------------------|
| Frontend | Netlify | [https://cafe-fausse.netlify.app](https://cafe-fausse.netlify.app) |
| Backend (API) | Render | [https://quantic-msse-webapp-interfacedesign.onrender.com](https://quantic-msse-webapp-interfacedesign.onrender.com) |

> Both are connected with shared API tokens and live database access.

---

## 🔐 Environment Variables

### Backend (`/backend/.env.sample`)
```env
FLASK_ENV=development
PORT=5000

# CORS / Frontend origin
NETLIFY_URL=http://localhost:5173

# Admin read-only token
ADMIN_TOKEN=dev-secret-123

# Database configuration
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cafe_fausse

DATABASE_URL=postgresql+pg8000://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

### Frontend (`/frontend/.env.sample`)
```env
VITE_API_URL=http://localhost:5000
VITE_ADMIN_TOKEN=dev-secret-123
```

---

## 📸 Image Credits
Images were created or curated using **Canva Pro** and organized into subfolders for clear categorization:

- **Dishes/** – menu items  
- **Catering/** – behind-the-scenes service  
- **Location/** – restaurant interiors/exteriors  
- **Behind the Scenes/** – team and event photos  

---

## 💬 Notes for Evaluation

✅ Meets all functional requirements (**FR-01 → FR-11**)  
✅ Newsletter & reservation forms connected to backend API endpoints  
✅ Gallery auto-groups and filters images by folder  
✅ Fully responsive and tested across desktop, tablet, and mobile  
✅ Code is modular, readable, and consistently named  

---

## 🤖 Acknowledgments
Created by **LaDonna Stephens** for the  
**Quantic School of Business and Technology**  
*Master of Science in Software Engineering – Web Application and Interface Design*

