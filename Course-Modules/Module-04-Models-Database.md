# Module 04 — Django Models and Database
**Duration: 1.5 Weeks | Get.TechAcad**

---

## Learning Objectives
- [ ] Define models using Django ORM
- [ ] Create and apply migrations
- [ ] Perform CRUD operations
- [ ] Use ForeignKey, ManyToMany, OneToOne relationships
- [ ] Query database efficiently

---

## Defining Models
```python
# portfolio/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title      = models.CharField(max_length=200)
    slug       = models.SlugField(unique=True)
    content    = models.TextField()
    thumbnail  = models.ImageField(upload_to='posts/', blank=True, null=True)
    published  = models.BooleanField(default=False)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

---

## Migrations
```bash
python manage.py makemigrations   # generate migration file
python manage.py migrate          # apply to database
python manage.py showmigrations   # view status
```

---

## CRUD Operations

### Create
```python
Post.objects.create(title="First Post", slug="first-post", content="Hello!", published=True)
```

### Read
```python
Post.objects.all()
Post.objects.filter(published=True)
Post.objects.get(pk=1)
Post.objects.filter(title__icontains='django').order_by('-created_at')[:5]
Post.objects.filter(published=True).count()
Post.objects.filter(slug='first-post').exists()
```

### Update
```python
post = Post.objects.get(pk=1)
post.title = "Updated Title"
post.save()

Post.objects.filter(published=False).update(published=True)
```

### Delete
```python
Post.objects.get(pk=1).delete()
Post.objects.filter(published=False).delete()
```

---

## Field Types Reference

| Field | Usage |
|-------|-------|
| `CharField(max_length=n)` | Short text |
| `TextField()` | Long text |
| `IntegerField()` | Whole number |
| `BooleanField()` | True/False |
| `DateTimeField(auto_now_add=True)` | Timestamp |
| `EmailField()` | Email |
| `ImageField(upload_to='dir/')` | Image file |
| `SlugField(unique=True)` | URL string |
| `ForeignKey()` | Many-to-one |
| `ManyToManyField()` | Many-to-many |
| `OneToOneField()` | One-to-one |

---

## Relationships
```python
# ForeignKey
category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
# Access: category.posts.all()

# ManyToMany
tags = models.ManyToManyField(Tag, blank=True)
# Access: post.tags.all(), post.tags.add(tag)

# OneToOne
user = models.OneToOneField(User, on_delete=models.CASCADE)
# Access: user.profile
```

---

## Mini-Project: Blog Application
Build a blog with Category, Post, Tag models. Display posts filtered by category in a template.

---
*Get.TechAcad | Module 04 of 12*
