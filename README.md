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

- Open terminal:

```bash
cd backend/server
```
- Activate virtual environment:
```bash
venv\Scripts\activate
```

-Install dependencies (if needed):
```bash
pip install django djangorestframework pandas django-cors-headers djangorestframework-simplejwt
```

-Run migrations:
```bash
python manage.py migrate
```

-Create admin user:
```bash
python manage.py createsuperuser
```

-Start server:
```bash
python manage.py runserver
```

#### Backend will run at:
```bash
http://127.0.0.1:8000
```

### 2. Web Frontend (React)

-Open new terminal:
```bash
cd web
npm install
npm start
```

#### Web app runs at:
```bash
http://localhost:3000
```

-Login using Django superuser credentials.

### 3. Desktop Application (PyQt5)

-Open another terminal:
```bash
cd desktop
python main.py
```

-Login using same credentials and upload CSV.

### API Endpoints

| Method | Endpoint              | Description                         |
|--------|----------------------|-------------------------------------|
| POST   | /api/token/          | Login and get JWT token             |
| POST   | /api/upload/         | Upload CSV file                     |
| GET    | /api/summary/latest/| Get latest summary statistics       |
| GET    | /api/history/        | Get upload history (Last 5)         |

### Sample Data

Use:
```text
sample_equipment_data.csv
```

for testing and demo.

### Notes

-Both web and desktop applications use the same Django backend.

-Only last 5 uploads are stored.

-Charts are generated using Chart.js (web) and Matplotlib (desktop).


## Quick Test Guide

1. Start Django backend.
2. Start React web app.
3. Login using admin credentials.
4. Upload `sample_equipment_data.csv`.
5. View summary and chart.

### For desktop:
1. Run `python main.py`
2. Login
3. Upload CSV
4. View chart popup.
