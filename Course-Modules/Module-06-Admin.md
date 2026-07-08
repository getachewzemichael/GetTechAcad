# Module 06 — Django Admin Panel
**Duration: 3 Days | Get.TechAcad**

---

## Learning Objectives
- [ ] Register models in the admin
- [ ] Customize list display, filters, and search
- [ ] Create superuser and access the admin panel
- [ ] Use admin actions

---

## Register Models
```python
# portfolio/admin.py
from django.contrib import admin
from .models import Post, Category, Tag, ContactMessage

admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ['title', 'category', 'published', 'created_at']
    list_filter         = ['published', 'category', 'created_at']
    search_fields       = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable       = ['published']
    date_hierarchy      = 'created_at'
    ordering            = ['-created_at']
    readonly_fields     = ['created_at', 'updated_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ['name', 'email', 'subject', 'created_at']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
```

---

## Create Superuser
```bash
python manage.py createsuperuser
# Enter: username, email, password
# Visit: http://127.0.0.1:8000/admin
```

---

## Customize Admin Site Header
```python
# admin.py
admin.site.site_header  = "Get.TechAcad Admin"
admin.site.site_title   = "Get.TechAcad"
admin.site.index_title  = "Welcome to Get.TechAcad Dashboard"
```

---

## Custom Admin Action
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(published=True)
        self.message_user(request, "Selected posts have been published.")
    make_published.short_description = "Mark selected posts as published"
```

---

## Task
1. Register all your models in admin
2. Customize list_display for each model
3. Add search and filter options
4. Create a superuser and log in

---
*Get.TechAcad | Module 06 of 12*
