# Knit Payment System

A simple payment system for schools, tracking payments and calculating school revenue with a 2% Knit fee.

---

## Setup Steps

### 1. Clone the repository
```bash
git clone https://github.com/PhalePallo/knit-payment-system.git
cd knit-payment-system
2. Setup Python virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
3. Install backend dependencies
pip install -r requirements.txt
4. Run the backend
python app.py

This will create the knit_payments.db SQLite database and seed initial schools and students.

Backend runs at http://127.0.0.1:5000

5. Setup and run frontend
cd frontend
npm install
npm start

React app runs at http://localhost:3000

Ensure the backend is running before using the frontend.

Assumptions Made

Each student belongs to exactly one school.

Knit fee is always 2% of the payment amount.

The remaining 98% goes to the school.

Payment reference must be unique to prevent duplicates.

Initial data seeded includes:

Schools: Greenwood High, Sunrise Academy

Students: Alice, Bob, Charlie

SQLite is used as the database for simplicity.

CORS is enabled to allow React frontend to communicate with Flask backend.

Improvements With More Time

Implement authentication for admins, students, and schools.

Add transaction history page for each student and school.

Enhance error handling and validation on both frontend and backend.

Replace SQLite with PostgreSQL for production.

Add unit tests for backend routes and frontend components.

Improve UI/UX using Tailwind or Material UI for a cleaner interface.

Support multiple payment methods (cards, mobile payments).

Implement real-time updates using WebSockets for revenue and payments.

Project Structure
knit-payment-system/
│
├─ backend/
│   ├─ app.py
│   ├─ models.py
│   ├─ routes/
│   │   ├─ payments.py
│   │   ├─ students.py
│   │   └─ schools.py
│   └─ knit_payments.db
│
├─ frontend/
│   ├─ src/
│   │   ├─ pages/
│   │   │   ├─ MakePayment.jsx
│   │   │   └─ SchoolRevenue.jsx
│   │   └─ api/
│   │       └─ api.js
│   ├─ package.json
│   └─ ...other React files
│
└─ README.md
Usage
Make a Payment

Select a student

Enter amount and reference

Click Pay

See the payment result

View School Revenue

Select a school

Click Get Revenue

View total collected, knit fees, and amount paid to school
