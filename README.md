# 📡 InfoTech Solutions - Backend API

This is the **Flask-based backend** for the InfoTech Solutions project, developed during my Web Development Internship. The backend handles form submissions for job applications, contact inquiries (career/cooperation), and basic login functionality — designed using scalable REST principles and deployed to the cloud.

---

## 🚀 Live API URL (Deployed on Render)
> 🌐 http://127.0.0.1:5000


---

## 🛠️ Tech Stack Used

- **Python 3**
- **Flask** — Web framework
- **Flask-SQLAlchemy** — ORM for database handling
- **Flask-Migrate** — Handles database migrations
- **Flask-CORS** — Cross-Origin support
- **SQLite** — Lightweight dev database
- **Postman** — API testing
- **Render** — Free cloud deployment with GitHub auto-deploy

---

## 📌 Features

- `POST /apply` — Job application with resume upload
- `POST /contact` — Handles both career and cooperation forms
- `GET /login` — Simple test login route
- File handling via `UPLOAD_FOLDER`
- Database migrations with `Flask-Migrate`

---

## 🔐 Auth Instructions

> No authentication is currently required — all endpoints are publicly accessible for development/testing purposes.

---

## 📫 API Endpoints & Usage

### 🔹 `POST /apply`

_Submit a job application with resume upload._

**Body Type:** `form-data`  
**Fields:**

| Key      | Example Value            |
|----------|--------------------------|
| name     | Aqsa                     |
| email    | aqsa@example.com         |
| phone    | 03001234567              |
| position | Backend Developer        |
| message  | Excited to apply!        |
| resume   | *(upload a PDF/DOC file)* |

POST /contact
Supports two modes: tab = "cooperation" or tab = "career"

Form-Data (career mode):

text
Copy
Edit
tab: career
firstName: Aqsa
lastName: Yaqoob
email: aqsa@example.com
phone: 03001234567
linkedIn: https://linkedin.com/in/aqsa
referral: From university
resume: (upload file)

Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/info_backend.git
cd info_backend
Create virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Initialize DB (with migration)

bash
Copy
Edit
$env:FLASK_APP = "run.py"
python -m flask db init
python -m flask db migrate -m "Initial migration"
python -m flask db upgrade
Run the server

bash
Copy
Edit
python run.py



