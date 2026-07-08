# Python-Django Full Stack Web Development
## Professional Course Guide

**Instructor:** Getachew Zemicheal Hadgu
**Institution:** Get.TechAcad — Tech + Growth
**Contact:** get.techacad@gmail.com
**Website:** https://gettechacad.onrender.com
**Edition:** 2025–2026

---

## About This Guide

This guide is the official lecture reference for the Python-Django Full Stack Web Development course delivered at Get.TechAcad. It is structured as a professional, hands-on curriculum that takes learners from zero programming knowledge to building and deploying real-world, production-ready web applications.

Each module contains:
- Learning objectives
- Detailed lecture notes with explanations
- Code examples with line-by-line commentary
- Hands-on exercises
- A practical mini-project
- A self-assessment quiz

---

## Course Structure at a Glance

| Module | Title | Duration |
|--------|-------|----------|
| 0 | Setup and Orientation | Day 1 |
| 1 | Python Fundamentals | 2 weeks |
| 2 | Web Fundamentals — HTML, CSS, Bootstrap | 1 week |
| 3 | Introduction to Django | 1 week |
| 4 | Django Models and Database | 1.5 weeks |
| 5 | Django Forms and Validation | 1 week |
| 6 | Django Admin Panel | 3 days |
| 7 | User Authentication and Authorization | 1 week |
| 8 | Class-Based Views | 4 days |
| 9 | Django REST Framework | 1.5 weeks |
| 10 | Frontend Integration and AJAX | 1 week |
| 11 | Deployment to Production | 4 days |
| 12 | Capstone Project | 2 weeks |

**Total Estimated Duration:**
- Part-time (2 hrs/day): 3–4 months
- Full-time (6 hrs/day): 6–8 weeks
- Intensive bootcamp: 4 weeks

---

## Prerequisites

No prior programming experience is required. Students should have:
- Basic computer operation skills
- Familiarity with using a web browser
- A computer with internet access (Windows, macOS, or Linux)

---

## Tools Required

| Tool | Version | Purpose | Download |
|------|---------|---------|----------|
| Python | 3.11+ | Programming language | python.org |
| VS Code | Latest | Code editor | code.visualstudio.com |
| Git | Latest | Version control | git-scm.com |
| Django | 5.x | Web framework | pip install django |
| PostgreSQL | 15+ | Production database | postgresql.org |
| Postman | Latest | API testing | postman.com |
| GitHub | — | Code repository | github.com |

---

# MODULE 0 — Setup and Orientation

## 0.1 Course Orientation

Welcome to the Python-Django Full Stack Web Development course. This course is designed to give you practical, industry-relevant skills that you can immediately apply to building real websites and web applications.

**What is Full Stack Development?**

Full stack development means you can build both:
- **The Frontend** — what users see (HTML, CSS, JavaScript, Bootstrap)
- **The Backend** — the server, database, and business logic (Python, Django)

By the end of this course you will be able to design, build, and deploy a complete web application entirely on your own.

---

## 0.2 Installing Python

1. Go to https://python.org/downloads
2. Download Python 3.11 or higher
3. During installation, check **"Add Python to PATH"** — this is critical
4. Verify installation by opening your terminal and typing:

```bash
python --version
```

Expected output:
```
Python 3.11.x
```

---

## 0.3 Installing VS Code

1. Go to https://code.visualstudio.com
2. Download and install for your operating system
3. Install the following extensions inside VS Code:
   - **Python** (by Microsoft)
   - **Django** (by Baptiste Darthenay)
   - **Prettier** (code formatter)
   - **GitLens** (Git integration)

---

## 0.4 Setting Up a Virtual Environment

A virtual environment isolates your project's dependencies from the global Python installation. This is professional best practice.

```bash
# Create a project folder
mkdir my_django_project
cd my_django_project

# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

---

## 0.5 Installing Django

```bash
pip install django
pip install pillow        # for image handling
pip install python-dotenv # for environment variables

# Verify
django-admin --version
```

---

# MODULE 1 — Python Fundamentals

## Learning Objectives

By the end of this module, students will be able to:
- Write and execute Python programs
- Use all core data types and data structures
- Apply conditional logic and loops
- Define and call functions
- Handle errors gracefully
- Apply Object-Oriented Programming principles

---

## 1.1 Variables and Data Types

A **variable** is a named container that stores a value. Python is dynamically typed — you do not need to declare the type.

```python
# String — text data
name = "Getachew Zemicheal"
city = 'Mekelle'

# Integer — whole numbers
age = 25
year = 2024

# Float — decimal numbers
cgpa = 3.83
price = 99.99

# Boolean — True or False
is_student = True
is_employed = False

# NoneType — represents absence of value
result = None

# Check type of a variable
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(cgpa))    # <class 'float'>
```

**Type Conversion:**

```python
age = "25"           # This is a string
age = int(age)       # Convert to integer
print(age + 5)       # 30

price = 99
price = float(price) # 99.0
price_str = str(99)  # "99"
```

---

## 1.2 String Operations

Strings are one of the most used data types in web development.

```python
first_name = "Getachew"
last_name  = "Zemicheal"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # Getachew Zemicheal

# f-strings (recommended for formatting)
greeting = f"Hello, {full_name}! Welcome to Get.TechAcad."
print(greeting)

# String methods
print(full_name.upper())        # GETACHEW ZEMICHEAL
print(full_name.lower())        # getachew zemicheal
print(full_name.replace("Getachew", "Get"))
print(full_name.split(" "))     # ['Getachew', 'Zemicheal']
print(len(full_name))           # 18

# Slicing
text = "Python Django"
print(text[0:6])    # Python
print(text[7:])     # Django
print(text[-6:])    # Django
```

---

## 1.3 Lists

A **list** is an ordered, mutable collection that can hold items of any type.

```python
courses = ["Python", "Django", "AI", "Digital Marketing"]

# Access by index (starts at 0)
print(courses[0])   # Python
print(courses[-1])  # Digital Marketing

# Add items
courses.append("Cybersecurity")
courses.insert(1, "HTML/CSS")

# Remove items
courses.remove("AI")
popped = courses.pop()   # removes and returns last item

# Loop through list
for course in courses:
    print(f"- {course}")

# List comprehension (professional shorthand)
upper_courses = [c.upper() for c in courses]

# Slicing
first_two = courses[:2]
last_two  = courses[-2:]

# Useful functions
print(len(courses))      # count
print(sorted(courses))   # sorted copy
print("Django" in courses)  # True/False check
```

---

## 1.4 Tuples and Sets

**Tuple** — ordered, immutable (cannot be changed after creation):

```python
coordinates = (9.1450, 40.4897)  # Mekelle coordinates
rgb_color   = (31, 218, 87)      # Get.TechAcad green

# Access
lat = coordinates[0]
lng = coordinates[1]

# Tuples are used when data should not change
```

**Set** — unordered, unique values only:

```python
skills = {"Python", "Django", "JavaScript", "Python"}
print(skills)  # {'Python', 'Django', 'JavaScript'} — no duplicates

skills.add("React")
skills.discard("JavaScript")

# Set operations
backend = {"Python", "Django", "PostgreSQL"}
frontend = {"HTML", "CSS", "Django"}

common = backend & frontend     # intersection: {'Django'}
all_skills = backend | frontend # union
```

---

## 1.5 Dictionaries

A **dictionary** stores data as key-value pairs. This is the foundation of how Django passes data to templates.

```python
student = {
    "name": "Getachew Zemicheal",
    "cgpa": 3.83,
    "university": "Mekelle University",
    "courses": ["Python", "Django", "AI"],
    "graduated": True
}

# Access values
print(student["name"])
print(student.get("cgpa", 0))  # safe access with default

# Modify
student["year"] = 2024
student["name"] = "Getachew Z. Hadgu"

# Loop through
for key, value in student.items():
    print(f"{key}: {value}")

# Check key exists
if "cgpa" in student:
    print("CGPA found:", student["cgpa"])

# Dictionary comprehension
scores = {"Math": 90, "Python": 95, "Django": 98}
passed = {subject: score for subject, score in scores.items() if score >= 90}
```

---

## 1.6 Conditional Statements

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# One-line ternary expression
status = "Pass" if score >= 50 else "Fail"

# Logical operators
age = 22
has_degree = True

if age >= 18 and has_degree:
    print("Eligible for the job")

if age < 18 or not has_degree:
    print("Not eligible")
```

---

## 1.7 Loops

**For loop:**

```python
# Loop over a range
for i in range(1, 6):
    print(f"Session {i}")

# Loop over a list
students = ["Abel", "Mekdes", "Yonas", "Tigist"]
for student in students:
    print(f"Welcome, {student}!")

# Enumerate — get index and value
for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")

# Loop over dictionary
profile = {"name": "Getachew", "role": "Instructor"}
for key, value in profile.items():
    print(f"{key} => {value}")
```

**While loop:**

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "techacad2024":
        print("Access granted!")
        break
    attempts += 1
    print(f"Wrong password. {max_attempts - attempts} attempts remaining.")
else:
    print("Account locked.")
```

---

## 1.8 Functions

Functions are reusable blocks of code. They are the building blocks of every Django view.

```python
# Basic function
def greet(name):
    return f"Hello, {name}! Welcome to Get.TechAcad."

message = greet("Getachew")
print(message)

# Function with default parameters
def calculate_grade(score, passing_score=50):
    if score >= passing_score:
        return "Pass"
    return "Fail"

print(calculate_grade(75))       # Pass (uses default)
print(calculate_grade(40, 45))   # Pass (custom passing score)

# Multiple return values
def get_name_parts(full_name):
    parts = full_name.split(" ")
    return parts[0], parts[-1]

first, last = get_name_parts("Getachew Zemicheal Hadgu")

# *args — variable number of arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))   # 15

# **kwargs — keyword arguments
def create_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(name="Getachew", role="Instructor", city="Mekelle")

# Lambda — anonymous one-line function
square = lambda x: x ** 2
print(square(5))  # 25

# Used with sorted()
students = [{"name": "Abel", "score": 88}, {"name": "Mekdes", "score": 95}]
ranked = sorted(students, key=lambda s: s["score"], reverse=True)
```

---

## 1.9 Error Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("This always runs.")

# Raise your own exception
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
```

---

## 1.10 Object-Oriented Programming (OOP)

OOP is how Django models, views, and forms are built. Understanding it is essential.

```python
# Define a class
class Student:
    # Class variable (shared by all instances)
    school = "Get.TechAcad"

    # Constructor — runs when object is created
    def __init__(self, name, cgpa):
        self.name = cgpa       # Instance variable
        self.cgpa = cgpa

    # Instance method
    def introduce(self):
        return f"I am {self.name} with CGPA {self.cgpa} from {self.school}."

    # String representation
    def __str__(self):
        return f"Student: {self.name}"

# Create objects (instances)
student1 = Student("Getachew", 3.83)
student2 = Student("Abel", 3.75)

print(student1.introduce())
print(student2)


# Inheritance
class GraduateStudent(Student):
    def __init__(self, name, cgpa, thesis_title):
        super().__init__(name, cgpa)    # Call parent constructor
        self.thesis_title = thesis_title

    def introduce(self):
        base = super().introduce()
        return f"{base} Thesis: {self.thesis_title}"


grad = GraduateStudent("Getachew", 3.83, "Sign Language Detection using AI")
print(grad.introduce())
```

---

## Module 1 Mini-Project: Student Grade Calculator

Build a CLI application that:
1. Accepts student names and scores for 5 subjects
2. Calculates average and letter grade
3. Displays a formatted report
4. Saves results to a text file

---

## Module 1 Quiz

1. What is the difference between a list and a tuple?
2. What does `self` represent in a class method?
3. Write a function that takes a list of numbers and returns only the even ones.
4. What is the purpose of `try-except`?
5. How do you add a new key-value pair to a dictionary?

---

# MODULE 2 — Web Fundamentals (HTML, CSS, Bootstrap)

## Learning Objectives

By the end of this module, students will be able to:
- Build structured web pages using semantic HTML
- Style pages using CSS including flexbox and grid
- Build responsive layouts using Bootstrap 5
- Understand how HTML, CSS, and Django templates connect

---

## 2.1 HTML Structure

Every web page is built on HTML (HyperText Markup Language). Django templates extend standard HTML.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Get.TechAcad</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <h1>Welcome to Get.TechAcad</h1>
    <nav>
      <a href="/home">Home</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
    </nav>
  </header>

  <main>
    <section>
      <h2>Our Courses</h2>
      <p>We offer Python, Django, AI, and Digital Marketing training.</p>
    </section>
  </main>

  <footer>
    <p>&copy; 2024 Get.TechAcad</p>
  </footer>

</body>
</html>
```

**Semantic HTML tags and their purpose:**

| Tag | Purpose |
|-----|---------|
| `<header>` | Top section — logo, navigation |
| `<nav>` | Navigation links |
| `<main>` | Primary content area |
| `<section>` | Thematic content grouping |
| `<article>` | Self-contained content (blog post) |
| `<aside>` | Sidebar content |
| `<footer>` | Bottom section |
| `<h1>`–`<h6>` | Headings (h1 is most important) |
| `<p>` | Paragraph |
| `<ul>`, `<ol>`, `<li>` | Lists |
| `<a>` | Hyperlink |
| `<img>` | Image |
| `<form>` | Form container |
| `<input>` | Form input field |
| `<button>` | Clickable button |
| `<table>` | Tabular data |

---

## 2.2 CSS Fundamentals

```css
/* Selecting by tag */
h1 {
  color: #1fda57;
  font-size: 2rem;
}

/* Selecting by class */
.card {
  background: #0a1628;
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid #1e3a2f;
}

/* Selecting by ID */
#hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
}

/* CSS Variables */
:root {
  --primary: #1fda57;
  --bg: #020d12;
  --text: #e0e6ed;
  --radius: 12px;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Poppins', sans-serif;
}
```

**CSS Box Model:**

Every HTML element is a box with:
- `content` — actual content
- `padding` — space inside the border
- `border` — the border line
- `margin` — space outside the border

```css
.box {
  width: 300px;
  padding: 20px;
  border: 2px solid var(--primary);
  margin: 10px auto;
}
```

**Flexbox — for one-dimensional layouts:**

```css
.navbar {
  display: flex;
  justify-content: space-between;  /* horizontal alignment */
  align-items: center;             /* vertical alignment */
  gap: 1rem;
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
}
```

**CSS Grid — for two-dimensional layouts:**

```css
.courses-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

/* Responsive grid */
@media (max-width: 768px) {
  .courses-grid {
    grid-template-columns: 1fr;
  }
}
```

---

## 2.3 Bootstrap 5

Bootstrap is a CSS framework that gives you pre-built, responsive components. Django projects commonly use Bootstrap for fast, professional styling.

**Including Bootstrap:**

```html
<!-- In your <head> -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Before closing </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

**Bootstrap Grid System:**

Bootstrap uses a 12-column grid. You define how many columns an element takes on each screen size.

```html
<div class="container">
  <div class="row g-4">

    <!-- Takes 4 columns on large screens, 6 on medium, full width on small -->
    <div class="col-lg-4 col-md-6 col-12">
      <div class="card">Course 1</div>
    </div>

    <div class="col-lg-4 col-md-6 col-12">
      <div class="card">Course 2</div>
    </div>

    <div class="col-lg-4 col-md-6 col-12">
      <div class="card">Course 3</div>
    </div>

  </div>
</div>
```

**Common Bootstrap Classes:**

```html
<!-- Buttons -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-outline-secondary">Outline</button>

<!-- Alerts -->
<div class="alert alert-success">Success message!</div>
<div class="alert alert-danger">Error message!</div>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="/">Get.TechAcad</a>
    <div class="navbar-nav ms-auto">
      <a class="nav-link" href="/about">About</a>
    </div>
  </div>
</nav>

<!-- Cards -->
<div class="card shadow">
  <div class="card-body">
    <h5 class="card-title">Python Django Course</h5>
    <p class="card-text">Learn full stack web development.</p>
    <a href="#" class="btn btn-primary">Enroll Now</a>
  </div>
</div>

<!-- Spacing utilities -->
<div class="mt-4 mb-3 px-2 py-3">Margin top 4, margin bottom 3, padding x 2, padding y 3</div>

<!-- Text utilities -->
<p class="text-center fw-bold text-success fs-5">Centered bold green text</p>
```

---

## Module 2 Mini-Project: Responsive Landing Page

Build a fully responsive landing page for Get.TechAcad using Bootstrap 5 that includes:
- Navigation bar with links
- Hero section with heading and button
- 3-column course cards section
- Contact form
- Footer with social links

---

# MODULE 3 — Introduction to Django

## Learning Objectives

By the end of this module, students will be able to:
- Explain Django's MVT architecture
- Create a Django project and app
- Define URL patterns and connect them to views
- Render templates with dynamic context data
- Work with static files

---

## 3.1 What is Django?

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. It follows the **MVT (Model-View-Template)** pattern:

| Component | Responsibility |
|-----------|---------------|
| **Model** | Defines data structure and interacts with the database |
| **View** | Contains business logic — receives requests, processes data, returns responses |
| **Template** | HTML files that display data to the user |

Django also has:
- **URL Dispatcher** — routes incoming URLs to the correct view
- **ORM** — abstracts database operations into Python code
- **Admin Panel** — built-in data management interface
- **Authentication** — built-in user login/logout/registration system
- **Security** — CSRF protection, SQL injection prevention, XSS protection built-in

---

## 3.2 Creating a Django Project

```bash
# Activate virtual environment first
venv\Scripts\activate  # Windows

# Install Django
pip install django

# Create project
django-admin startproject gettechacad .
# The dot (.) creates files in the current folder

# Project structure created:
# gettechacad/
#   __init__.py
#   settings.py   ← project configuration
#   urls.py       ← main URL routing
#   wsgi.py       ← web server interface
#   asgi.py       ← async server interface
# manage.py       ← command-line utility

# Run the development server
python manage.py runserver
# Visit: http://127.0.0.1:8000
```

---

## 3.3 Creating a Django App

A Django **project** is the entire website. A Django **app** is a component of the project.

```bash
# Create an app
python manage.py startapp portfolio

# App structure:
# portfolio/
#   migrations/   ← database migration files
#   __init__.py
#   admin.py      ← register models for admin
#   apps.py       ← app configuration
#   models.py     ← database models
#   tests.py      ← automated tests
#   views.py      ← request handlers
```

**Register the app in settings.py:**

```python
# gettechacad/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',    # ← add your app here
]
```

---

## 3.4 Views

A **view** is a Python function (or class) that receives a web request and returns a web response.

```python
# portfolio/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Simple text response
def hello(request):
    return HttpResponse("Hello from Get.TechAcad!")

# Rendering a template
def home(request):
    context = {
        "name": "Getachew Zemicheal",
        "role": "Technology Instructor",
        "courses": ["Python", "Django", "AI", "Digital Marketing"],
    }
    return render(request, "portfolio/home.html", context)
```

---

## 3.5 URL Configuration

URLs connect incoming web requests to the correct view function.

```python
# portfolio/urls.py  (create this file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
]
```

```python
# gettechacad/urls.py  (main URL file)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # include app URLs
]
```

---

## 3.6 Templates

Templates are HTML files with Django Template Language (DTL) for dynamic content.

**Folder structure:**
```
templates/
  base.html
  portfolio/
    home.html
    about.html
```

**Configure template directory in settings.py:**

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← tell Django where templates are
        'APP_DIRS': True,
        ...
    },
]
```

**base.html — the parent template:**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <title>{% block title %}Get.TechAcad{% endblock %}</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
  </nav>

  <main>
    {% block content %}
    {% endblock %}
  </main>

  <footer>
    <p>&copy; 2024 Get.TechAcad</p>
  </footer>
</body>
</html>
```

**home.html — child template:**

```html
{% extends 'base.html' %}

{% block title %}Home | Get.TechAcad{% endblock %}

{% block content %}
<h1>Welcome, {{ name }}</h1>
<p>Role: {{ role }}</p>

<h2>Courses Offered:</h2>
<ul>
  {% for course in courses %}
    <li>{{ course }}</li>
  {% endfor %}
</ul>

{% if courses %}
  <p>We have {{ courses|length }} courses available.</p>
{% else %}
  <p>No courses available yet.</p>
{% endif %}
{% endblock %}
```

**DTL — Django Template Language Quick Reference:**

| Syntax | Purpose |
|--------|---------|
| `{{ variable }}` | Output variable value |
| `{% tag %}` | Template logic tags |
| `{% for x in list %}...{% endfor %}` | Loop |
| `{% if condition %}...{% endif %}` | Conditional |
| `{% extends 'base.html' %}` | Inherit parent template |
| `{% block name %}...{% endblock %}` | Define replaceable block |
| `{% url 'name' %}` | Generate URL by name |
| `{% static 'path' %}` | Link to static file |
| `{% load static %}` | Load static files tag |
| `{{ value\|filter }}` | Apply filter to value |

---

## 3.7 Static Files

Static files are CSS, JavaScript, and images that don't change per request.

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

**Folder structure:**
```
static/
  css/
    style.css
  js/
    main.js
  images/
    logo.png
```

**Using static files in templates:**

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/main.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

## Module 3 Mini-Project: Multi-Page Django Portfolio

Build a Django portfolio site with:
- Home, About, Contact pages
- Shared base template with navigation
- Context data passed from views to templates
- Static CSS for styling

---

# MODULE 4 — Django Models and Database

## Learning Objectives

By the end of this module, students will be able to:
- Define database models using Django's ORM
- Create and apply migrations
- Perform full CRUD operations using the ORM
- Define model relationships
- Query the database efficiently

---

## 4.1 What is an ORM?

An **ORM (Object Relational Mapper)** lets you work with databases using Python objects instead of raw SQL. Django's ORM translates Python code into SQL automatically.

```python
# Without ORM (raw SQL)
cursor.execute("SELECT * FROM portfolio_post WHERE published = TRUE")

# With Django ORM (Python)
posts = Post.objects.filter(published=True)
```

---

## 4.2 Defining Models

```python
# portfolio/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    # Field types
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)
    content     = models.TextField()
    excerpt     = models.CharField(max_length=300, blank=True)
    thumbnail   = models.ImageField(upload_to='posts/', blank=True, null=True)
    published   = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
```

**Common Field Types:**

| Field | Use Case |
|-------|---------|
| `CharField(max_length=n)` | Short text (names, titles) |
| `TextField()` | Long text (descriptions, content) |
| `IntegerField()` | Whole numbers |
| `FloatField()` | Decimal numbers |
| `BooleanField()` | True/False |
| `DateField()` | Date only |
| `DateTimeField()` | Date and time |
| `EmailField()` | Email addresses (with validation) |
| `URLField()` | URLs |
| `ImageField()` | Image files |
| `FileField()` | Any file |
| `SlugField()` | URL-friendly strings |
| `ForeignKey()` | Many-to-one relationship |
| `ManyToManyField()` | Many-to-many relationship |
| `OneToOneField()` | One-to-one relationship |

**Field options:**

```python
name = models.CharField(
    max_length=100,
    blank=True,    # allows empty in forms
    null=True,     # allows NULL in database
    default="",    # default value
    unique=True,   # must be unique
    db_index=True, # creates database index for faster queries
)
```

---

## 4.3 Migrations

Migrations are Django's way of applying model changes to the database.

```bash
# Step 1: Generate migration file from model changes
python manage.py makemigrations

# Step 2: Apply migrations to the database
python manage.py migrate

# View migration SQL without applying
python manage.py sqlmigrate portfolio 0001

# Show migration status
python manage.py showmigrations
```

**Important rule:** Every time you change a model (add/remove/modify a field), you must run `makemigrations` then `migrate`.

---

## 4.4 CRUD Operations with ORM

**CREATE:**

```python
# Method 1: create()
post = Post.objects.create(
    title="Django ORM Tutorial",
    slug="django-orm-tutorial",
    content="This is the content...",
    published=True
)

# Method 2: save()
post = Post()
post.title = "Django ORM Tutorial"
post.slug = "django-orm-tutorial"
post.content = "This is the content..."
post.save()
```

**READ:**

```python
# Get all records
all_posts = Post.objects.all()

# Get single record by primary key
post = Post.objects.get(id=1)
post = Post.objects.get(pk=1)

# Get single record — safer (returns None if not found)
post = Post.objects.filter(id=1).first()

# Filter records
published = Post.objects.filter(published=True)
recent    = Post.objects.filter(created_at__year=2024)
popular   = Post.objects.filter(views_count__gte=100)

# Exclude records
drafts = Post.objects.exclude(published=True)

# Order records
newest = Post.objects.all().order_by('-created_at')
oldest = Post.objects.all().order_by('created_at')

# Limit records
top_5 = Post.objects.all()[:5]

# Count records
count = Post.objects.filter(published=True).count()

# Check existence
exists = Post.objects.filter(slug='django-tutorial').exists()

# Search — case-insensitive contains
results = Post.objects.filter(title__icontains='django')
```

**UPDATE:**

```python
# Update single record
post = Post.objects.get(id=1)
post.title = "Updated Title"
post.save()

# Bulk update
Post.objects.filter(published=False).update(published=True)
```

**DELETE:**

```python
# Delete single record
post = Post.objects.get(id=1)
post.delete()

# Bulk delete
Post.objects.filter(published=False).delete()
```

---

## 4.5 Model Relationships

**ForeignKey — Many posts belong to one category:**

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title    = models.CharField(max_length=200)
    content  = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,    # delete posts if category deleted
        related_name='posts'
    )
```

```python
# Query related data
category = Category.objects.get(slug='technology')
posts = category.posts.all()       # all posts in this category

post = Post.objects.get(id=1)
print(post.category.name)          # access the related category
```

**ManyToManyField — Posts can have many tags, tags can have many posts:**

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags  = models.ManyToManyField(Tag, blank=True)
```

```python
post = Post.objects.get(id=1)
post.tags.add(Tag.objects.get(name='Django'))
post.tags.all()       # get all tags for this post
post.tags.remove(tag) # remove a tag
```

**OneToOneField — Each user has one profile:**

```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    bio    = models.TextField(blank=True)
    photo  = models.ImageField(upload_to='profiles/', blank=True)
    phone  = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
```

---

## Module 4 Mini-Project: Blog App

Build a blog application with:
- `Category`, `Post`, `Tag` models
- ForeignKey and ManyToMany relationships
- All CRUD operations tested in Django shell
- Posts displayed in a template grouped by category

---

# MODULE 5 — Django Forms and Validation

## Learning Objectives

By the end of this module, students will be able to:
- Create and render Django forms
- Use ModelForm to auto-generate forms from models
- Validate form input (built-in and custom)
- Handle file uploads
- Display success/error messages

---

## 5.1 Creating a Django Form

```python
# portfolio/forms.py
from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=100)
    email   = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    # Custom validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if email and 'spam' in message.lower():
            raise forms.ValidationError("Spam messages are not allowed.")
        return cleaned_data
```

---

## 5.2 ModelForm

`ModelForm` automatically generates a form from a model.

```python
from django import forms
from .models import Post, ContactMessage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
            'title':   forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'published': 'Publish immediately',
        }

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
```

---

## 5.3 Handling Forms in Views

```python
# portfolio/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Access cleaned data
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Process (save to DB, send email, etc.)
            form.save()  # if using ModelForm

            messages.success(request, "Your message was sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ContactForm()  # empty form for GET request

    return render(request, 'portfolio/contact.html', {'form': form})
```

---

## 5.4 Rendering Forms in Templates

```html
{% extends 'base.html' %}
{% block content %}

<h2>Contact Us</h2>

{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }}">{{ message }}</div>
  {% endfor %}
{% endif %}

<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}

  {% for field in form %}
    <div class="mb-3">
      <label class="form-label">{{ field.label }}</label>
      {{ field }}
      {% if field.errors %}
        <div class="text-danger">
          {% for error in field.errors %}
            <small>{{ error }}</small>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  {% endfor %}

  <button type="submit" class="btn btn-primary">Send Message</button>
</form>

{% endblock %}
```

---

# MODULE 6 — Django Admin Panel

## Learning Objectives

By the end of this module, students will be able to:
- Register models with the admin panel
- Customize list display, filters, and search
- Use admin to manage all site data

---

## 6.1 Registering Models

```python
# portfolio/admin.py
from django.contrib import admin
from .models import Post, Category, Tag, ContactMessage

# Basic registration
admin.site.register(Category)
admin.site.register(Tag)

# Custom admin class
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display   = ['title', 'category', 'published', 'created_at']
    list_filter    = ['published', 'category', 'created_at']
    search_fields  = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable  = ['published']
    date_hierarchy = 'created_at'
    ordering       = ['-created_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
```

**Create superuser:**

```bash
python manage.py createsuperuser
# Enter username, email, password
# Visit: http://127.0.0.1:8000/admin
```

---

# MODULE 7 — User Authentication

## Learning Objectives

By the end of this module, students will be able to:
- Implement user registration, login, and logout
- Protect views with `@login_required`
- Extend the User model with a Profile
- Reset passwords via email

---

## 7.1 Built-in Authentication Views

```python
# urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/',    auth_views.LoginView.as_view(template_name='auth/login.html'),    name='login'),
    path('logout/',   auth_views.LogoutView.as_view(),                                  name='logout'),
    path('register/', views.register,                                                   name='register'),
    path('profile/',  views.profile,                                                    name='profile'),
]
```

## 7.2 Registration View

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
```

## 7.3 Protecting Views

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')
```

## 7.4 Extended User Profile

```python
# models.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    bio   = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# Auto-create profile when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

---

# MODULE 8 — Class-Based Views

## Learning Objectives

By the end of this module, students will be able to:
- Use Django's built-in CBVs for common CRUD patterns
- Override CBV methods to customize behavior
- Apply mixins for authentication

---

## 8.1 Common Class-Based Views

```python
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PostListView(ListView):
    model               = Post
    template_name       = 'portfolio/post_list.html'
    context_object_name = 'posts'
    paginate_by         = 10
    ordering            = ['-created_at']

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model               = Post
    template_name       = 'portfolio/post_detail.html'
    context_object_name = 'post'
    slug_field          = 'slug'


class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    form_class    = PostForm
    template_name = 'portfolio/post_form.html'
    success_url   = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = 'portfolio/post_form.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model       = Post
    success_url = reverse_lazy('post-list')
```

```python
# urls.py
urlpatterns = [
    path('posts/',          PostListView.as_view(),   name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/',   PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
```

---

# MODULE 9 — Django REST Framework

## Learning Objectives

By the end of this module, students will be able to:
- Build a fully functional REST API with Django
- Create serializers for data conversion
- Implement authentication and permissions
- Test APIs using Postman

---

## 9.1 Setup

```bash
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

## 9.2 Serializers

```python
# portfolio/serializers.py
from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'category', 'category_id', 'published', 'created_at']
        read_only_fields = ['id', 'slug', 'created_at']
```

## 9.3 API Views

```python
# portfolio/api_views.py
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPI(generics.ListCreateAPIView):
    queryset         = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field     = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

```python
# urls.py
from .api_views import PostListCreateAPI, PostRetrieveUpdateDestroyAPI

urlpatterns += [
    path('api/posts/',          PostListCreateAPI.as_view(),            name='api-posts'),
    path('api/posts/<slug:slug>/', PostRetrieveUpdateDestroyAPI.as_view(), name='api-post-detail'),
]
```

---

# MODULE 10 — Frontend Integration

## Learning Objectives

By the end of this module, students will be able to:
- Fetch data from Django APIs using JavaScript
- Implement live search without page refresh
- Display dynamic data in templates

---

## 10.1 AJAX with Fetch API

```javascript
// static/js/main.js

// Live search example
const searchInput = document.getElementById('search');
const resultsDiv  = document.getElementById('results');

searchInput.addEventListener('input', async function() {
    const query = this.value.trim();
    if (query.length < 2) {
        resultsDiv.innerHTML = '';
        return;
    }

    try {
        const response = await fetch(`/api/posts/?search=${query}`);
        const data     = await response.json();

        resultsDiv.innerHTML = data.results.map(post => `
            <div class="search-result">
                <a href="/posts/${post.slug}/">${post.title}</a>
                <p>${post.excerpt}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Search failed:', error);
    }
});
```

```python
# Django view that returns JSON
from django.http import JsonResponse

def search_api(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        title__icontains=query,
        published=True
    ).values('title', 'slug', 'excerpt')[:10]
    return JsonResponse({'results': list(posts)})
```

---

# MODULE 11 — Deployment to Production

## Learning Objectives

By the end of this module, students will be able to:
- Configure Django for production
- Deploy to Render with PostgreSQL
- Serve static and media files correctly

---

## 11.1 Production Settings

```python
# settings.py
import os
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG      = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['yourdomain.onrender.com', 'localhost']

# Database
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )
    }

# Static files
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
```

## 11.2 build.sh for Render

```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Auto-create superuser
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
email    = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created.')
"
```

## 11.3 Required Environment Variables on Render

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Long random string |
| `DEBUG` | `False` |
| `DATABASE_URL` | PostgreSQL connection string |
| `CLOUDINARY_CLOUD_NAME` | From Cloudinary dashboard |
| `CLOUDINARY_API_KEY` | From Cloudinary dashboard |
| `CLOUDINARY_API_SECRET` | From Cloudinary dashboard |
| `EMAIL_HOST_USER` | Gmail address |
| `EMAIL_HOST_PASSWORD` | Gmail App Password |
| `DJANGO_SUPERUSER_USERNAME` | Admin username |
| `DJANGO_SUPERUSER_PASSWORD` | Admin password |

---

# MODULE 12 — Capstone Project

## Project Brief

Build a complete, production-deployed web application demonstrating all skills learned in this course.

## Requirements Checklist

- [ ] Django project with at least 2 apps
- [ ] Minimum 4 database models with relationships
- [ ] Full CRUD operations on at least one model
- [ ] User authentication (register, login, logout)
- [ ] Django forms with validation
- [ ] REST API endpoint (at least one)
- [ ] Django admin panel configured
- [ ] Responsive Bootstrap 5 frontend
- [ ] Static and media files working
- [ ] Deployed to Render (production)
- [ ] PostgreSQL database
- [ ] Environment variables configured
- [ ] GitHub repository

## Suggested Project Ideas

| Project | Complexity |
|---------|-----------|
| Personal Portfolio Website | ⭐⭐ |
| Blog Platform with Categories | ⭐⭐⭐ |
| Job Board | ⭐⭐⭐ |
| Student Management System | ⭐⭐⭐ |
| Training Booking Platform | ⭐⭐⭐⭐ |
| E-commerce Product Catalog | ⭐⭐⭐⭐ |

## Evaluation Criteria

| Criteria | Weight |
|----------|--------|
| Functionality — all features work | 30% |
| Code quality — clean, organized, commented | 20% |
| Database design — proper models and relationships | 20% |
| UI/UX — responsive, professional design | 15% |
| Deployment — live and accessible | 15% |

---

# Appendix A — Django Cheat Sheet

## Project Setup

```bash
python -m venv venv && venv\Scripts\activate
pip install django
django-admin startproject projectname .
python manage.py startapp appname
python manage.py runserver
```

## Database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
```

## ORM Quick Reference

```python
Model.objects.all()
Model.objects.filter(field=value)
Model.objects.exclude(field=value)
Model.objects.get(pk=1)
Model.objects.create(field=value)
Model.objects.filter(field=value).update(field=new_value)
Model.objects.filter(field=value).delete()
Model.objects.order_by('-created_at')[:10]
Model.objects.filter(name__icontains='query')
Model.objects.count()
Model.objects.filter(...).exists()
```

## URL Patterns

```python
path('', views.home, name='home')
path('<int:pk>/', views.detail, name='detail')
path('<slug:slug>/', views.detail, name='detail')
path('<str:username>/', views.profile, name='profile')
```

---

# Appendix B — Recommended Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| Django Official Docs | docs.djangoproject.com | Primary reference |
| Django REST Framework | django-rest-framework.org | API development |
| Bootstrap 5 | getbootstrap.com/docs | Frontend components |
| Python Docs | docs.python.org | Python reference |
| Real Python | realpython.com | Tutorials and guides |
| GitHub | github.com | Code hosting |
| Render | render.com | Deployment |
| Neon | neon.tech | Free PostgreSQL |
| Cloudinary | cloudinary.com | Media storage |

---

*This guide is prepared and maintained by **Getachew Zemicheal Hadgu***
*Founder — Get.TechAcad | BSc Computer Science & Engineering, Mekelle University*
*📧 get.techacad@gmail.com | 🌐 gettechacad.onrender.com*
*© 2025–2026 Get.TechAcad. All rights reserved.*
