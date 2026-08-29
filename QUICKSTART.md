# Django Admin Pro - Quick Start Guide

Get up and running in under 5 minutes!

---

## 🚀 Quick Start with Docker (Recommended)

### Prerequisites
- Docker & Docker Compose installed
- Git installed

### Steps

```bash
# 1. Clone the repository
git clone <repo-url>
cd django-admin-pro

# 2. Copy environment variables
cp .env.example .env

# 3. Start services
docker-compose up -d

# 4. Run migrations
docker-compose exec web python manage.py migrate

# 5. Create demo data
docker-compose exec web python manage.py create_demo_data

# 6. Access the app
# Dashboard: http://localhost:8000/dashboard/
# Admin Panel: http://localhost:8000/admin/
# API Swagger Docs: http://localhost:8000/api/docs/
```

**Demo Credentials:**
- Email: `owner@example.com`
- Password: `password123`

---

## 🐍 Local Setup (Without Docker)

### Prerequisites
- Python 3.11+
- pip & virtualenv

### Steps

```bash
# 1. Clone the repository
git clone <repo-url>
cd django-admin-pro

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment variables
cp .env.example .env

# 5. Run migrations
python manage.py migrate

# 6. Create demo data
python manage.py create_demo_data

# 7. Start development server
python manage.py runserver
```

---

## 📝 Common Commands

### Database
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

### Users
```bash
# Create superuser
python manage.py createsuperuser

# Seed demo data
python manage.py create_demo_data

# Change user password
python manage.py changepassword email@example.com
```

### Development & Testing
```bash
# Run tests
python manage.py test

# Django shell
python manage.py shell
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic --noinput

# Clear static files and collect again
python manage.py collectstatic --clear --noinput
```

---

## 🔌 API Examples

### Authentication

```bash
# Sign up
curl -X POST http://localhost:8000/api/auth/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@example.com",
    "password": "securepass123",
    "first_name": "John",
    "last_name": "Doe"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "owner@example.com",
    "password": "password123"
  }'

# Get current user profile
curl -X GET http://localhost:8000/api/auth/users/profile/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### Dashboard Analytics

```bash
# Get stats
curl -X GET http://localhost:8000/api/dashboard/stats/

# Get signup chart data
curl -X GET "http://localhost:8000/api/dashboard/chart-signups/?months=6"
```

---

## 🛠️ Customization

### Customizing User Model
The project uses a custom `CustomUser` model located in `apps/accounts/models.py`.

To add new fields to the user model:
```python
class CustomUser(AbstractUser):
    # Add custom fields here
    company = models.CharField(max_length=255, blank=True)
```

Then create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 💬 Support & Help

- Read [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment instructions.
- Email support: support@djangoadminpro.com
