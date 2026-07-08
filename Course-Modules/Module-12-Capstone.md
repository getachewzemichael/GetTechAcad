# Module 12 — Capstone Project
**Duration: 2 Weeks | Get.TechAcad**

---

## Overview

The Capstone Project is your opportunity to demonstrate everything learned across all 12 modules. You will design, build, and deploy a complete full stack web application from scratch — independently.

---

## Requirements Checklist

### Django & Backend
- [ ] Django project with at least 2 apps
- [ ] Minimum 4 database models with relationships (ForeignKey, ManyToMany or OneToOne)
- [ ] Full CRUD operations on at least 2 models
- [ ] `__str__`, `Meta`, and proper field choices defined
- [ ] Migrations applied cleanly

### Authentication
- [ ] User registration and login
- [ ] Logout
- [ ] At least one `@login_required` protected view
- [ ] Profile model with OneToOneField to User

### Forms
- [ ] At least 2 forms (one ModelForm, one custom form)
- [ ] Server-side validation with error display
- [ ] File/image upload working

### Admin
- [ ] All models registered in admin
- [ ] list_display, search_fields, list_filter configured
- [ ] Custom admin site title and header

### REST API
- [ ] At least 2 API endpoints using DRF
- [ ] Serializers for all API models
- [ ] Token authentication on protected endpoints
- [ ] Tested and documented in Postman

### Frontend
- [ ] Bootstrap 5 responsive design
- [ ] Shared base.html with template inheritance
- [ ] At least 6 pages
- [ ] At least 1 AJAX feature (search, live update, etc.)

### Deployment
- [ ] Live on Render
- [ ] PostgreSQL via Neon
- [ ] Media on Cloudinary
- [ ] `DEBUG=False` in production
- [ ] UptimeRobot monitoring active
- [ ] GitHub repository with clean commit history

---

## Suggested Project Ideas

### Option A — Training Booking Platform ⭐⭐⭐⭐
A platform where students can browse courses and book training sessions.

**Models:** Course, Booking, Trainer, Student Profile
**Features:** Course listing, booking form, admin management, API for course list

---

### Option B — Job Board ⭐⭐⭐
A job listing platform where companies post jobs and candidates apply.

**Models:** Company, Job, Application, User Profile
**Features:** Job listing, search/filter, application form, employer dashboard

---

### Option C — Student Management System ⭐⭐⭐
A system to manage students, courses, grades, and attendance.

**Models:** Student, Course, Enrollment, Grade
**Features:** Admin dashboard, grade entry, attendance tracking, reports

---

### Option D — E-commerce Product Catalog ⭐⭐⭐⭐
A product catalog where vendors list products and customers browse.

**Models:** Category, Product, Order, Review
**Features:** Product listing, cart, checkout form, admin panel, product API

---

### Option E — Personal Portfolio + Blog ⭐⭐
A full portfolio site with a blog, contact form, and project showcase.

**Models:** Post, Category, Project, ContactMessage
**Features:** Blog with search, project gallery, contact form, admin

---

## Evaluation Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| Functionality | 30% | All required features work correctly |
| Code Quality | 20% | Clean, organized, commented code |
| Database Design | 20% | Proper models and relationships |
| UI/UX Design | 15% | Responsive, professional, accessible |
| Deployment | 15% | Live, stable, environment configured |

---

## Submission Requirements

1. **Live URL** — deployed Render link
2. **GitHub Repository** — clean commit history
3. **Admin credentials** — for evaluation
4. **Postman collection** — exported API tests
5. **Short README.md** — project description, setup steps, features

---

## README.md Template
```markdown
# Project Name

## Description
Brief description of your project.

## Features
- Feature 1
- Feature 2
- Feature 3

## Tech Stack
- Python 3.11
- Django 5.x
- PostgreSQL (Neon)
- Bootstrap 5
- Cloudinary
- Deployed on Render

## Setup (Local)
```bash
git clone https://github.com/yourusername/yourproject
cd yourproject
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # fill in your values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Environment Variables
See `.env.example` for required variables.

## Live Demo
https://yourproject.onrender.com

## Admin
/admin/ (credentials provided separately)
```

---

## Final Presentation

Each student will present their project in a 10-minute session covering:

1. **Demo** (5 min) — show the live site, walk through features
2. **Code walkthrough** (3 min) — explain one model and one view
3. **Q&A** (2 min) — answer instructor questions

---

## Congratulations!

By completing this capstone you have demonstrated the ability to:
- Design and build a database-backed web application
- Implement user authentication and security
- Build and consume REST APIs
- Deploy a production-ready Django application
- Use professional tools: Git, GitHub, Postman, Render, Neon, Cloudinary

You are now a **Python-Django Full Stack Developer**.

---
*Get.TechAcad | Module 12 of 12 — Final Module*
*Instructor: Getachew Zemicheal Hadgu*
*📧 get.techacad@gmail.com | 🌐 gettechacad.onrender.com*
