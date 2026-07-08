# Module 03 — Introduction to Django
**Duration: 1 Week | Get.TechAcad**

---

## Learning Objectives
- [ ] Explain Django's MVT architecture
- [ ] Create a Django project and app
- [ ] Define URL patterns and connect to views
- [ ] Render templates with dynamic context data
- [ ] Use static files in templates

---

## Django MVT Architecture

| Layer | File | Role |
|-------|------|------|
| Model | models.py | Data structure, database |
| View | views.py | Business logic, request handling |
| Template | templates/*.html | HTML output to the browser |
| URL | urls.py | Routes URL to the correct view |

---

## Create Project and App
```bash
django-admin startproject gettechacad .
python manage.py startapp portfolio

# Register app in settings.py
INSTALLED_APPS = [..., 'portfolio']
```

---

## Views
```python
# portfolio/views.py
from django.shortcuts import render

def home(request):
    context = {
        "name": "Getachew Zemicheal",
        "courses": ["Python", "Django", "AI"],
    }
    return render(request, "portfolio/home.html", context)
```

---

## URL Routing
```python
# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

# gettechacad/urls.py
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
```

---

## Templates

**base.html**
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}Get.TechAcad{% endblock %}</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
  </nav>
  <main>{% block content %}{% endblock %}</main>
  <footer><p>&copy; 2024 Get.TechAcad</p></footer>
</body>
</html>
```

**home.html**
```html
{% extends 'base.html' %}
{% block title %}Home | Get.TechAcad{% endblock %}
{% block content %}
  <h1>Welcome, {{ name }}</h1>
  <ul>
    {% for course in courses %}
      <li>{{ course }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```

---

## Django Template Language (DTL) Quick Reference

| Syntax | Purpose |
|--------|---------|
| `{{ variable }}` | Display value |
| `{% for x in list %}` | Loop |
| `{% if condition %}` | Conditional |
| `{% url 'name' %}` | Reverse URL |
| `{% static 'path' %}` | Static file path |
| `{% extends 'base.html' %}` | Inherit template |
| `{% block name %}` | Replaceable block |
| `{{ value\|length }}` | Filter |

---

## Static Files Setup
```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## Mini-Project: Multi-Page Portfolio Site
Build a Django portfolio with Home, About, and Contact pages using template inheritance and static CSS.

---
*Get.TechAcad | Module 03 of 12*
