# Django Admin Pro - Project Structure

```
django-admin-pro/
│
├── 📄 Core Configuration Files
│   ├── manage.py                    # Django management CLI
│   ├── Dockerfile                   # Docker image configuration
│   ├── docker-compose.yml           # Docker services
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Environment variables template
│   ├── .gitignore                   # Git ignore patterns
│   ├── setup.sh                     # Linux/Mac setup script
│   └── setup.bat                    # Windows setup script
│
├── 📚 Documentation
│   ├── README.md                    # Main documentation & feature overview
│   ├── QUICKSTART.md                # Quick start guide (5 min setup)
│   ├── DEPLOYMENT.md                # Production deployment guide
│   └── PROJECT_STRUCTURE.md         # This structure guide
│
├── 🔧 Config Package
│   ├── config/
│   │   ├── __init__.py              # Config init
│   │   ├── settings.py              # Django settings (DB, Auth, Email, etc.)
│   │   ├── urls.py                  # URL routing
│   │   ├── wsgi.py                  # WSGI application
│   │   └── asgi.py                  # ASGI application
│
└── 📱 Apps Directory
    └── apps/
        │
        ├── accounts/                # User authentication & management
        │   ├── models.py            # CustomUser, PasswordReset models
        │   ├── views.py             # AuthViewSet, UserViewSet, signup_view
        │   ├── serializers.py       # DRF serializers for user profiles
        │   ├── urls.py              # API routes
        │   ├── admin.py             # Django admin configuration
        │   ├── forms.py             # User change/creation forms
        │   ├── apps.py              # App configuration
        │   ├── tests.py             # Unit tests
        │   ├── __init__.py
        │   └── management/
        │       ├── __init__.py
        │       └── commands/
        │           ├── __init__.py
        │           └── create_demo_data.py  # Seeds database with demo users
        │
        ├── dashboard/               # Dashboard views & metrics
        │   ├── models.py            # Dashboard preferences model
        │   ├── views.py             # Dashboard pages rendering
        │   ├── serializers.py       # Dashboard stats serializer
        │   ├── urls.py              # API routes
        │   ├── views_urls.py        # Template view routes
        │   ├── admin.py             # Django admin
        │   ├── apps.py              # App configuration
        │   ├── tests.py             # Unit tests
        │   └── migrations/
        │
        └── core/                    # Core utilities & helpers
            ├── utils.py             # Email and data export helpers
            ├── decorators.py        # Authentication & staff checks
            ├── permissions.py       # DRF custom permissions (IsAdminUser)
            ├── models.py            # Core configurations
            ├── admin.py             # Core admin
            └── apps.py              # App configuration
```

---

## 🎨 Templates Structure

```
templates/
├── base.html                # Base layout with layout styling
├── sidebar.html             # Mobile-responsive navigation sidebar
├── registration/            # User account template pages
│   ├── login.html           # Dark mode glassmorphism login page
│   └── signup.html          # Neo-Brutalist registration page
└── dashboard/               # Dashboard templates
    ├── home.html            # Metrics & signups chart
    ├── users.html           # Superuser user-database administration table
    ├── profile.html         # User profile views
    └── settings.html        # Preferences and account settings
```

---

## 📦 Key Features Summary

### Authentication System
- ✅ Email-based signup/login (no username required)
- ✅ Secure token-based password reset flow
- ✅ Customized signup and profile page layout

### Dashboard & Analytics
- ✅ Pre-built metric cards (Total users, Active, Verified)
- ✅ Chart.js integration showing monthly user signups
- ✅ Fully responsive navigation design
- ✅ Dark/Light mode toggle powered by Alpine.js

### Frontend Stack
- ✅ Tailwind CSS (utility-first styling)
- ✅ Alpine.js (reactive state and light/dark mode)
- ✅ HTMX (dynamic operations without full page reload)
- ✅ Chart.js (beautiful metrics graphs)

### Technology Stack
- **Backend**: Django 4.2.x, Django REST Framework 3.14.x, SQLite 3
- **Frontend**: Tailwind CSS 3, Alpine.js 3, HTMX 1.9, Chart.js 4.4
- **DevOps**: Docker & Docker Compose
