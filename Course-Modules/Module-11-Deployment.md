# Module 11 — Deployment to Production
**Duration: 4 Days | Get.TechAcad**

---

## Learning Objectives
- [ ] Configure Django for production
- [ ] Serve static files with WhiteNoise
- [ ] Store media files on Cloudinary
- [ ] Connect to PostgreSQL via Neon
- [ ] Deploy to Render
- [ ] Configure all environment variables securely

---

## 11.1 Why Production is Different from Development

| Setting | Development | Production |
|---------|-------------|------------|
| DEBUG | True | False |
| Database | SQLite (file) | PostgreSQL (server) |
| Static files | Served by Django | Served by WhiteNoise/CDN |
| Media files | Local disk | Cloudinary |
| SECRET_KEY | Can be simple | Must be long and secret |
| HTTPS | Not required | Required |

---

## 11.2 Install Production Packages
```bash
pip install gunicorn whitenoise dj-database-url psycopg2-binary cloudinary django-cloudinary-storage
pip freeze > requirements.txt
```

---

## 11.3 Production Settings
```python
# settings.py
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG      = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'yourdomain.onrender.com',
    '127.0.0.1',
    'localhost',
]

CSRF_TRUSTED_ORIGINS = [
    'https://yourdomain.onrender.com',
]

# ===== DATABASE =====
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ===== STATIC FILES =====
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← must be second
    ...
]

# ===== CLOUDINARY MEDIA =====
CLOUDINARY_STORAGE = {
    'CLOUD_NAME':  os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY':     os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET':  os.environ.get('CLOUDINARY_API_SECRET'),
    'SECURE':      True,
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

import cloudinary
cloudinary.config(secure=True)

# ===== SECURITY (production only) =====
if not DEBUG:
    SECURE_SSL_REDIRECT            = True
    SESSION_COOKIE_SECURE          = True
    CSRF_COOKIE_SECURE             = True
    SECURE_HSTS_SECONDS            = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD            = True
    SECURE_BROWSER_XSS_FILTER      = True
```

---

## 11.4 build.sh (Render Build Script)
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Auto-create superuser from environment variables
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
email    = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser created: {username}')
else:
    print(f'Superuser already exists: {username}')
"
```

---

## 11.5 render.yaml (Optional Service Config)
```yaml
services:
  - type: web
    name: gettechacad
    env: python
    buildCommand: './build.sh'
    startCommand: 'gunicorn gettechacad.wsgi:application'
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## 11.6 Environment Variables on Render

Go to Render Dashboard → Your Service → **Environment** tab and add:

| Variable | Where to Get |
|----------|-------------|
| `SECRET_KEY` | Generate: `python -c "import secrets; print(secrets.token_urlsafe(50))"` |
| `DEBUG` | Set to `False` |
| `DATABASE_URL` | Neon dashboard → Connection string |
| `CLOUDINARY_CLOUD_NAME` | cloudinary.com/console |
| `CLOUDINARY_API_KEY` | cloudinary.com/console |
| `CLOUDINARY_API_SECRET` | cloudinary.com/console |
| `EMAIL_HOST_USER` | Your Gmail address |
| `EMAIL_HOST_PASSWORD` | Gmail App Password |
| `DJANGO_SUPERUSER_USERNAME` | Choose a username |
| `DJANGO_SUPERUSER_PASSWORD` | Choose a strong password |
| `DJANGO_SUPERUSER_EMAIL` | Your email |

---

## 11.7 Setting Up Free PostgreSQL on Neon

1. Go to https://neon.tech → Sign up
2. Click **Create Project** → name it, choose region
3. Copy the **Connection string**:
   ```
   postgresql://username:password@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
   ```
4. Paste into Render as `DATABASE_URL`

**Why Neon?** Unlike Render's free PostgreSQL (expires after 90 days), Neon's free tier has no expiry.

---

## 11.8 Deployment Checklist

- [ ] `requirements.txt` is up to date
- [ ] `build.sh` is executable and correct
- [ ] `DEBUG=False` in production
- [ ] `ALLOWED_HOSTS` includes your Render domain
- [ ] All environment variables set on Render
- [ ] Neon PostgreSQL created and `DATABASE_URL` set
- [ ] Cloudinary credentials set
- [ ] `collectstatic` runs without errors
- [ ] `migrate` runs without errors
- [ ] Admin login works at `/admin/`
- [ ] Site loads without 500 errors
- [ ] Static files (CSS/JS) load correctly
- [ ] Media files (images) load correctly

---

## 11.9 Keep Your Site Awake (UptimeRobot)

Render free tier sleeps after 15 minutes of inactivity. Fix it:

1. Go to https://uptimerobot.com → Sign up free
2. Add New Monitor → HTTP(s)
3. URL: `https://yourdomain.onrender.com`
4. Interval: **5 minutes**
5. Save

Your site will never sleep again.

---

## Task
Deploy your blog application from Module 04 to production on Render with Neon PostgreSQL and Cloudinary.

---
*Get.TechAcad | Module 11 of 12*
