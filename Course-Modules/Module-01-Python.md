# Module 01 — Python Fundamentals
**Duration: 2 Weeks | Get.TechAcad**

---

## Learning Objectives
- [ ] Variables and data types
- [ ] Lists, tuples, sets, dictionaries
- [ ] Conditional statements and loops
- [ ] Functions (basic, default args, *args, **kwargs)
- [ ] Error handling with try/except
- [ ] Object-Oriented Programming

---

## Week 1: Core Python

### Variables and Types
```python
name  = "Getachew"   # str
age   = 25           # int
cgpa  = 3.83         # float
active = True        # bool
```

### Lists
```python
courses = ["Python", "Django", "AI"]
courses.append("Marketing")
for c in courses:
    print(c)
```

### Dictionaries
```python
student = {"name": "Abel", "cgpa": 3.75}
print(student["name"])
student["year"] = 2024
```

### Conditionals and Loops
```python
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"

for i in range(1, 6):
    print(f"Session {i}")
```

---

## Week 2: Functions and OOP

### Functions
```python
def greet(name, title="Student"):
    return f"Hello {title} {name}!"

def add(*nums):
    return sum(nums)
```

### OOP
```python
class Student:
    school = "Get.TechAcad"
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
    def __str__(self):
        return f"{self.name} — {self.cgpa}"

class GradStudent(Student):
    def __init__(self, name, cgpa, thesis):
        super().__init__(name, cgpa)
        self.thesis = thesis
```

---

## Mini-Project: Grade Calculator
Build a CLI program that:
1. Accepts name and 5 subject scores
2. Calculates average and letter grade
3. Saves report to a .txt file

---

## Quiz
1. What is the difference between a list and a tuple?
2. What does `self` mean in a class?
3. Write a function returning only even numbers from a list.
4. What does `try/except` do?

---
*Get.TechAcad | Module 01 of 12*
