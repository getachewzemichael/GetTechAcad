# Module 00 — Setup and Orientation
**Python-Django Full Stack Web Development**
**Get.TechAcad | Instructor: Getachew Zemicheal Hadgu**

---

## Session Goals
By the end of this session, students will have:
- A fully working Python development environment
- Django installed and a test project running
- VS Code configured with all required extensions

---

## Step 1: Install Python
1. Go to https://python.org/downloads
2. Download Python 3.11 or higher
3. ✅ Check **"Add Python to PATH"** during installation
4. Verify: `python --version`

## Step 2: Install VS Code
1. Go to https://code.visualstudio.com
2. Install extensions: Python, Django, Prettier, GitLens

## Step 3: Virtual Environment
```bash
mkdir my_project && cd my_project
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux
```

## Step 4: Install Django
```bash
pip install django pillow python-dotenv
django-admin --version
```

## Step 5: First Django Project
```bash
django-admin startproject mysite .
python manage.py runserver
# Visit: http://127.0.0.1:8000
```

---

## Homework
- Install all tools
- Run the Django welcome page
- Take a screenshot as proof of completion

---
*Get.TechAcad | Module 00 of 12*
