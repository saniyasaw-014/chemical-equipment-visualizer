# Chemical Equipment Parameter Visualizer

This is a hybrid **Web + Desktop application** built as part of an intern screening task.

The project allows users to upload a CSV file containing chemical equipment data and view summary statistics and charts. A single Django backend is used by both the React web app and the PyQt5 desktop app.

---

## Features

- **Data Ingestion:** Upload CSV file containing equipment data.
- **Automated Analysis:** Automatic data analysis using Pandas.
- **Summary Statistics:**
  - Total equipment count
  - Average flowrate
  - Average pressure
  - Average temperature
- **Visualizations:** Equipment type distribution chart.
- **Authentication:** JWT based authentication.
- **History:** Tracks the last 5 uploaded datasets.
- **Dual Frontend:**
  - Web frontend using React + Chart.js
  - Desktop application using PyQt5 + Matplotlib

---

## Tech Stack

**Backend:**
- Python
- Django
- Django REST Framework
- Pandas
- SQLite

**Web Frontend:**
- React.js
- Chart.js

**Desktop Frontend:**
- PyQt5
- Matplotlib

**Authentication:**
- JWT (SimpleJWT)

---

## Project Structure

```text
chemical-equipment-visualizer/
│
├── backend/
│   └── server/
│       ├── api/
│       │   ├── migrations/
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── models.py
│       │   ├── urls.py
│       │   ├── utils.py
│       │   └── views.py
│       │
│       ├── server/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       │
│       ├── manage.py
│       └── db.sqlite3
│
├── web/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── UploadCSV.js
│   │   │   ├── Summary.js
│   │   │   ├── Charts.js
│   │   │   └── History.js
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.js
│   │   └── index.js
│   │
│   └── package.json
│
├── desktop/
│   ├── main.py
│   ├── api_client.py
│   └── charts.py
│
├── sample_equipment_data.csv
└── README.md
```

---

## Setup Instructions

### 1. Backend (Django)

#### 1.1: Open terminal:

```bash
cd backend/server
```
#### 1.2: Activate virtual environment:
```bash
venv\Scripts\activate
```

#### 1.3: Install dependencies (if needed):
```bash
pip install django djangorestframework pandas django-cors-headers djangorestframework-simplejwt
```

#### 1.4: Run migrations:
```bash
python manage.py migrate
```

Create admin user:

python manage.py createsuperuser


Start server:

python manage.py runserver


Backend will run at:

http://127.0.0.1:8000

2. Web Frontend (React)

Open new terminal:

cd web
npm install
npm start


Web app runs at:

http://localhost:3000


Login using Django superuser credentials.

3. Desktop Application (PyQt5)

Open another terminal:

cd desktop
python main.py


Login using same credentials and upload CSV.

API Endpoints

POST /api/token/ – Login and get JWT token

POST /api/upload/ – Upload CSV file

GET /api/summary/latest/ – Latest summary

GET /api/history/ – Upload history

Sample Data

Use the provided file:

sample_equipment_data.csv


for testing and demo.

Notes

Both web and desktop applications use the same Django backend.

Only last 5 uploads are stored.

Charts are generated using Chart.js (web) and Matplotlib (desktop).
