# Django Admin Pro - Starter Dashboard Boilerplate

**Django Admin Pro (Starter Tier)** is a production-ready dashboard boilerplate built with Django, Tailwind CSS, Alpine.js, and HTMX. It provides a clean, modern start for developers looking to build customer-facing admin panels or SaaS interfaces without the overhead of complex, heavyweight services.

---

## 🚀 Features

### ✅ Authentication & User Profiles
- **Email-based authentication** - Login and sign up using email address (no username required).
- **Secure registration** - Built-in sign-up form with custom validation.
- **Password reset flow** - Secure token-based password recovery.
- **User profiles** - Supports user avatars, bios, phone numbers, and account verification status.

### 📊 Dashboard & Analytics
- **Pre-built metric cards** - Track total users, active users, and verified users.
- **Chart.js integration** - Interactive visualization of user signup trends.
- **Responsive design** - Mobile-first layout styled with Tailwind CSS, Alpine.js, and HTMX.

### 🎨 Neo-Brutalist UI Design
- **Stark styling** - Bold components with thick black borders (3px) and harsh drop shadows.
- **Theme control** - Persistent Dark/Light mode toggle powered by Alpine.js.
- **Dynamic updates** - Seamless interactions and form submissions without page reloads using HTMX.

### 🔧 Developer Experience
- **Dockerized setup** - Docker Compose configuration for immediate containerized deployment.
- **Local setup** - Easy local setup option using a virtual environment and SQLite.
- **REST API** - Standard endpoints with Django REST Framework (DRF), complete with Swagger/ReDoc auto-generated documentation.

---

## 📁 Project Structure

```
django-admin-pro/
├── config/                  # Django settings & URL routing
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/                    # Django apps
│   ├── accounts/           # User authentication, profiles, and views
│   ├── dashboard/          # Dashboard views, templates, and analytics APIs
│   └── core/               # Utilities, decorators, and permission classes
├── templates/              # HTML templates (Tailwind + Alpine.js + HTMX)
├── static/                 # Static files (CSS, JavaScript)
├── manage.py               # Django management command CLI
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker image configuration
├── requirements.txt        # Python dependencies
└── .env.example            # Environment variables example template
```

---

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose (recommended) OR Python 3.11+

### Option 1: With Docker (Recommended)

1. **Clone the repository and navigate inside**
   ```bash
   git clone <repo-url>
   cd django-admin-pro
   ```

2. **Copy the environment file**
   ```bash
   cp .env.example .env
   ```

3. **Start the containers**
   ```bash
   docker-compose up -d
   ```

4. **Run migrations and create demo data**
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py create_demo_data
   ```

5. **Access the application**
   - **Dashboard**: http://localhost:8000/dashboard/
   - **Admin Panel**: http://localhost:8000/admin/
   - **API Swagger Docs**: http://localhost:8000/api/docs/

---

### Option 2: Local Setup (Without Docker)

1. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Copy environment variables**
   ```bash
   cp .env.example .env
   ```

4. **Run migrations and seed demo data**
   ```bash
   python manage.py migrate
   python manage.py create_demo_data
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Credentials & Access

Default credentials seeded by `create_demo_data`:
- **Admin/Superuser**:
  - Email: `owner@example.com`
  - Password: `password123`
- **Standard Users**:
  - Email: `manager@example.com` | Password: `password123`
  - Email: `viewer@example.com` | Password: `password123`

---

## 🔌 API Documentation

Django Admin Pro automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

---

## 🧪 Testing

Run tests locally with:
```bash
python manage.py test
```
