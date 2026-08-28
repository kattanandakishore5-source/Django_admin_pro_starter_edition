# Django Admin Pro - Deployment Guide

This guide covers deploying the Django Admin Pro Starter Tier dashboard to production environments.

---

## 🔒 Security Checklist

Before deploying to production, ensure you complete the following checklist:

- [ ] Set `DEBUG = False` in your environment.
- [ ] Generate a unique, secure `SECRET_KEY`.
- [ ] Configure `ALLOWED_HOSTS` with your production domain name(s).
- [ ] Configure a secure production database.
- [ ] Set up HTTPS/SSL on your web server.
- [ ] Ensure HTTPS-only session and CSRF cookie flags are enabled.
- [ ] Configure CORS allowed origins correctly.

---

## Environment Variables

Configure your production server using a secure environment file or platform variables:

```bash
# Django Configuration
DEBUG=False
SECRET_KEY=your-long-random-secret-key-change-this
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (PostgreSQL recommended in production)
DB_NAME=django_admin_pro_prod
DB_USER=db_user
DB_PASSWORD=strong-secure-password
DB_HOST=db.yourdomain.com
DB_PORT=5432

# Email settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key

# S3 File Storage (Optional)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1
```

---

## Deployment Options

### Option 1: DigitalOcean App Platform

1. **Create PostgreSQL Database**
   - In the DigitalOcean Console, provision a managed PostgreSQL database.
   - Secure the connection and record the connection string.

2. **Push Code to GitHub**
   ```bash
   git add .
   git commit -m "Configure production deployment"
   git push origin main
   ```

3. **Deploy via App Platform**
   - Connect your GitHub repository to the App Platform.
   - Choose the branch to deploy.
   - Bind the App database service to your PostgreSQL instance.
   - Define your environment variables in the App Console.
   - Deploy the application.

---

### Option 2: Heroku

1. **Install Heroku CLI and Login**
   ```bash
   heroku login
   ```

2. **Create App and Add-Ons**
   ```bash
   heroku create your-app-name
   heroku addons:create heroku-postgresql:essential-0
   ```

3. **Configure Procfile**
   Ensure you have a `Procfile` containing the release and web server commands:
   ```txt
   release: python manage.py migrate
   web: gunicorn config.wsgi:application --log-file -
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

---

### Option 3: Standard Linux VPS (Ubuntu/Nginx/Gunicorn)

1. **Install System Dependencies**
   ```bash
   sudo apt update && sudo apt install -y python3-pip nginx gunicorn git
   ```

2. **Clone and Configure**
   ```bash
   git clone <your-repo-url>
   cd django-admin-pro
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Gunicorn Service**
   Create a systemd unit file at `/etc/systemd/system/gunicorn.service`:

   ```ini
   [Unit]
   Description=Gunicorn Django Admin Pro
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/django-admin-pro
   Environment="PATH=/home/ubuntu/django-admin-pro/venv/bin"
   ExecStart=/home/ubuntu/django-admin-pro/venv/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock config.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

4. **Configure Nginx Site Configuration**
   Create `/etc/nginx/sites-available/django-admin-pro`:

   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;
       
       location / {
           include proxy_params;
           proxy_pass http://unix:/run/gunicorn.sock;
       }
       
       location /static/ {
           alias /home/ubuntu/django-admin-pro/staticfiles/;
       }
   }
   ```

   Link the site and start Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/django-admin-pro /etc/nginx/sites-enabled/
   sudo systemctl enable nginx gunicorn
   sudo systemctl restart nginx gunicorn
   ```

---

## Performance Optimization & Monitoring

- **Static Assets**: Configure `django-storages` or Nginx to serve static files. Always run `python manage.py collectstatic` on deployment.
- **Sentry Integration**: Install `sentry-sdk` and configure it in `settings.py` to track runtime exceptions and errors.
