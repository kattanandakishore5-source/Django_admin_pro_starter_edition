# Django Admin Pro - Setup Instructions

## ✅ Project Setup Guide

Your Django Admin Pro Starter Tier dashboard boilerplate is ready. Below are the details of the stack and instructions to customize and run it.

---

## 📦 What's Included

### ✨ Core Features
- **Email-based Authentication** - Signup and login using email address (no username required).
- **Password Reset Flow** - Secure token-based password recovery.
- **Neo-Brutalist UI Theme** - High-contrast dashboard using thick black borders and sharp shadows.
- **Responsive Layout** - Styled with Tailwind CSS, Alpine.js, and HTMX.

### 📊 Dashboard & Metrics
- **Metric Cards** - Real-time statistics including Total Users, Active Users, and Verified Users.
- **Signup Charts** - User signup trends visualized with Chart.js.
- **Responsive Navigation** - Side menu sidebar with persistence controls.

### 🚀 Developer Experience
- **Docker Compose** - One-command containerized setup for easy execution.
- **Django REST Framework** - Out-of-the-box REST API for profiles and analytics.
- **Swagger/ReDoc** - Automatically generated API documentation.
- **Comprehensive Tests** - Built-in test cases for accounts and dashboard apps.
- **Demo Data Seeding** - CLI command to populate test data in seconds.

---

## 🚀 Quick Start (Choose One)

### Option 1: Docker (Recommended) ⭐
**Time: 2 minutes**

```bash
cd django-admin-pro
cp .env.example .env
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py create_demo_data
```

✅ Access your dashboard at: http://localhost:8000/dashboard/

---

### Option 2: Automated Script Setup
**Time: 3 minutes**

```bash
cd django-admin-pro

# On Linux/Mac
chmod +x setup.sh
./setup.sh

# On Windows
setup.bat
```

---

### Option 3: Manual Local Setup
**Time: 4 minutes**

```bash
cd django-admin-pro
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py create_demo_data
python manage.py runserver
```

---

## 🔐 Credentials & URLs

**Demo credentials (seeded by default):**
```
Email: owner@example.com
Password: password123
```

### Access URLs
- **Dashboard**: http://localhost:8000/dashboard/
- **Admin Panel**: http://localhost:8000/admin/
- **API Swagger Docs**: http://localhost:8000/api/docs/
- **API ReDoc Docs**: http://localhost:8000/api/redoc/

---

## 🛠️ Common Commands

### Database Migrations
```bash
python manage.py makemigrations   # Create migrations
python manage.py migrate          # Apply migrations
```

### Seeding & Admin Users
```bash
python manage.py createsuperuser  # Create Django admin
python manage.py create_demo_data # Seed initial database
```

### Testing
```bash
python manage.py test             # Run all unit tests
```

---

## 💻 Tech Stack Summary

- **Backend**: Django 4.2.x, Django REST Framework 3.14.x, SQLite 3
- **Frontend**: Tailwind CSS, Alpine.js, HTMX, Chart.js
- **Containerization**: Docker, Docker Compose
