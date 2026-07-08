# Python-Django Full Stack Web Development
## Student Workbook

**Student Name:** ___________________________________
**Enrollment Date:** _________________________________
**Instructor:** Getachew Zemicheal Hadgu — Get.TechAcad
**Contact:** get.techacad@gmail.com

---

## How to Use This Workbook

- Complete each exercise before moving to the next module
- Write your answers and code in the spaces provided
- Mark your progress using the checkboxes
- Bring this workbook to every session

---

# MODULE 00 — Setup Checklist

- [ ] Python installed — version: _______________
- [ ] VS Code installed
- [ ] Python extension installed in VS Code
- [ ] Django extension installed in VS Code
- [ ] Virtual environment created
- [ ] Django installed — version: _______________
- [ ] Test project runs at http://127.0.0.1:8000

**Notes / Issues I faced during setup:**

```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

---

# MODULE 01 — Python Fundamentals

## Exercise 1.1 — Variables
Write a Python program that stores your name, age, city, and CGPA, then prints them using an f-string.

**Your code:**
```python
# Write here




```

**Expected output:**
```
My name is ___, I am ___ years old, from ___, CGPA: ___
```

---

## Exercise 1.2 — Lists and Loops
Create a list of 5 technologies you want to learn. Loop through the list and print each one numbered.

**Your code:**
```python
# Write here




```

---

## Exercise 1.3 — Dictionary
Create a dictionary representing a student profile with name, age, university, cgpa, and a list of courses. Print all key-value pairs.

**Your code:**
```python
# Write here




```

---

## Exercise 1.4 — Functions
Write a function called `calculate_grade(score)` that returns:
- "A" for 90–100
- "B" for 80–89
- "C" for 70–79
- "D" for 60–69
- "F" below 60

**Your code:**
```python
# Write here




```

---

## Exercise 1.5 — OOP
Create a `Course` class with attributes: `name`, `duration`, `price`. Add a method `describe()` that returns a formatted string. Create 3 course objects.

**Your code:**
```python
# Write here




```

---

## Module 01 — Self-Assessment

Rate your confidence (1=Low, 5=High):

| Topic | Confidence (1–5) |
|-------|-----------------|
| Variables and data types | |
| Lists and dictionaries | |
| Loops and conditionals | |
| Functions | |
| OOP / Classes | |
| Error handling | |

**Questions I still have:**
```
_______________________________________________________________
_______________________________________________________________
```

---

# MODULE 02 — Web Fundamentals

## Exercise 2.1 — HTML Structure
Build an HTML page for Get.TechAcad with a header, navigation, one course card, and a footer.

**Your file: index.html**
```html
<!-- Write your HTML here -->




```

---

## Exercise 2.2 — Bootstrap Grid
Using Bootstrap 5, create a 3-column responsive grid of course cards that stacks to 1 column on mobile.

**Your code:**
```html
<!-- Write here -->




```

---

## Module 02 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| HTML semantic structure | |
| CSS flexbox | |
| Bootstrap grid | |
| Responsive design | |

---

# MODULE 03 — Introduction to Django

## Exercise 3.1 — Create Project and App
Write the commands to:
1. Create a Django project called `techacad`
2. Create an app called `courses`
3. Run the development server

**Commands:**
```bash
# 1.

# 2.

# 3.
```

---

## Exercise 3.2 — View and URL
Write a view function called `course_list` that passes a list of 3 courses to a template. Then write the URL pattern for it.

**views.py:**
```python
# Write here




```

**urls.py:**
```python
# Write here




```

---

## Exercise 3.3 — Template
Write a Django template that loops through a `courses` list and displays each course in a Bootstrap card.

**courses.html:**
```html
{% extends 'base.html' %}
{% block content %}
<!-- Write here -->


{% endblock %}
```

---

## Module 03 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| MVT architecture | |
| URL routing | |
| Function-based views | |
| Django template language | |
| Static files | |

---

# MODULE 04 — Models and Database

## Exercise 4.1 — Define a Model
Write a `Course` model with: title (CharField), description (TextField), price (DecimalField), is_active (BooleanField), created_at (DateTimeField auto).

**models.py:**
```python
# Write here




```

---

## Exercise 4.2 — ORM Queries
Write ORM queries for:
1. Get all active courses
2. Get the first course ordered by price (lowest first)
3. Count all courses
4. Update all courses to is_active=True
5. Get courses where title contains "Python"

**Your answers:**
```python
# 1.

# 2.

# 3.

# 4.

# 5.
```

---

## Exercise 4.3 — Relationships
Draw the relationships between these models:
- A `Category` has many `Courses`
- A `Course` has many `Tags`
- A `Course` has one `Instructor`

**Write the model code:**
```python
# Write here




```

---

## Module 04 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| Defining models | |
| Migrations | |
| ORM queries | |
| Model relationships | |
| Django shell | |

---

# MODULE 05 — Forms and Validation

## Exercise 5.1 — Create a BookingForm
Create a ModelForm for a `Booking` model with fields: name, email, course, message. Add validation that the name must be at least 3 characters.

**forms.py:**
```python
# Write here




```

---

## Exercise 5.2 — Handle Form in View
Write a view that handles GET (show empty form) and POST (validate and save). Show success message on redirect.

**views.py:**
```python
# Write here




```

---

## Module 05 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| Django forms | |
| ModelForm | |
| Form validation | |
| CSRF protection | |
| Flash messages | |

---

# MODULE 06 — Django Admin

## Exercise 6.1 — Register and Customize
Register your `Course` model in admin with:
- list_display: title, category, is_active, created_at
- search_fields: title, description
- list_filter: category, is_active
- list_editable: is_active

**admin.py:**
```python
# Write here




```

---

## Module 06 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| Registering models | |
| Customizing ModelAdmin | |
| Admin actions | |
| Creating superuser | |

---

# MODULE 07 — Authentication

## Exercise 7.1 — Registration View
Write a registration view using `UserCreationForm` that logs the user in after successful registration.

**views.py:**
```python
# Write here




```

---

## Exercise 7.2 — Profile Model
Write a `Profile` model with a OneToOneField to User and signals to auto-create it.

**models.py:**
```python
# Write here




```

---

## Module 07 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| Login / Logout | |
| Registration | |
| @login_required | |
| Profile model | |
| Django signals | |

---

# MODULE 08 — Class-Based Views

## Exercise 8.1 — Rewrite Using CBV
Rewrite your course_list view from Module 03 as a `ListView`. Add pagination (5 per page).

**views.py:**
```python
# Write here




```

**urls.py:**
```python
# Write here


```

---

## Module 08 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| ListView | |
| DetailView | |
| CreateView | |
| UpdateView / DeleteView | |
| LoginRequiredMixin | |

---

# MODULE 09 — Django REST Framework

## Exercise 9.1 — Serializer
Write a `CourseSerializer` that includes: id, title, description, price, is_active, category name.

**serializers.py:**
```python
# Write here




```

---

## Exercise 9.2 — API View
Write a `ListCreateAPIView` for courses that requires authentication for creating, but allows read without auth.

**api_views.py:**
```python
# Write here




```

---

## Exercise 9.3 — Postman Test
Document your API test results:

| Endpoint | Method | Status Code | Notes |
|----------|--------|-------------|-------|
| /api/courses/ | GET | | |
| /api/courses/ | POST | | |
| /api/courses/1/ | GET | | |
| /api/courses/1/ | PUT | | |
| /api/courses/1/ | DELETE | | |
| /api/token/ | POST | | |

---

## Module 09 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| REST concepts | |
| Serializers | |
| Generic API views | |
| Token authentication | |
| Postman testing | |

---

# MODULE 10 — Frontend Integration

## Exercise 10.1 — AJAX Search
Write a Django view that returns JSON search results for courses by title. Write the JavaScript fetch code to call it.

**views.py:**
```python
# Write here




```

**JavaScript:**
```javascript
// Write here




```

---

## Module 10 — Self-Assessment

| Topic | Confidence (1–5) |
|-------|-----------------|
| Fetch API | |
| JSON responses in Django | |
| Debouncing | |
| CSRF with AJAX | |

---

# MODULE 11 — Deployment

## Deployment Checklist

- [ ] requirements.txt updated
- [ ] build.sh created
- [ ] Neon PostgreSQL created
- [ ] DATABASE_URL set on Render
- [ ] Cloudinary account created and keys set
- [ ] All env vars configured on Render
- [ ] Site deployed and accessible
- [ ] Admin panel working on production
- [ ] UptimeRobot monitoring configured

**My deployed site URL:** ________________________________

**Issues I faced during deployment:**
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

---

# MODULE 12 — Capstone Project

## Project Plan

**Project Title:** _______________________________________

**Description:**
```
_______________________________________________________________
_______________________________________________________________
```

**Models I will build:**

| Model | Fields | Relationships |
|-------|--------|---------------|
| | | |
| | | |
| | | |
| | | |

**Pages / URLs I will create:**

| URL | View | Template |
|-----|------|----------|
| / | | |
| /about/ | | |
| | | |
| | | |

**API Endpoints I will build:**

| Endpoint | Method | Auth Required |
|----------|--------|---------------|
| | | |
| | | |

---

## Weekly Progress Log

**Week 1:**
```
Day 1: ___________________________________________________
Day 2: ___________________________________________________
Day 3: ___________________________________________________
Day 4: ___________________________________________________
Day 5: ___________________________________________________
```

**Week 2:**
```
Day 1: ___________________________________________________
Day 2: ___________________________________________________
Day 3: ___________________________________________________
Day 4: ___________________________________________________
Day 5: ___________________________________________________
```

---

## Final Submission

**Live URL:** _____________________________________________
**GitHub URL:** __________________________________________
**Admin Username:** ______________________________________

---

## Course Completion Reflection

**What I learned that I did not know before:**
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**The most challenging part was:**
```
_______________________________________________________________
_______________________________________________________________
```

**I want to learn next:**
```
_______________________________________________________________
_______________________________________________________________
```

---

*Congratulations on completing the Python-Django Full Stack Web Development Course!*
*You are now a Full Stack Django Developer.*

---

**Certified by:**

Getachew Zemicheal Hadgu
Instructor — Get.TechAcad
📧 get.techacad@gmail.com
🌐 gettechacad.onrender.com

**Date of Completion:** _____________________________

**Signature:** _____________________________
