# Module 05 — Django Forms and Validation
**Duration: 1 Week | Get.TechAcad**

---

## Learning Objectives
- [ ] Create and render Django forms
- [ ] Use ModelForm
- [ ] Validate input (built-in and custom)
- [ ] Handle file uploads
- [ ] Display flash messages

---

## Django Form
```python
# portfolio/forms.py
from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=100)
    email   = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name
```

---

## ModelForm
```python
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'content', 'category', 'published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
            'title':   forms.TextInput(attrs={'class': 'form-control'}),
        }
```

---

## Handling in View
```python
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form.cleaned_data contains validated values
            form.save()  # only for ModelForm
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
```

---

## Template Rendering
```html
<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% for field in form %}
    <div class="mb-3">
      <label>{{ field.label }}</label>
      {{ field }}
      {% for error in field.errors %}
        <small class="text-danger">{{ error }}</small>
      {% endfor %}
    </div>
  {% endfor %}
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

---

## Flash Messages
```html
{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }}">{{ message }}</div>
  {% endfor %}
{% endif %}
```

---

## Mini-Project: Contact Form with Email
Build a contact page with form validation that saves messages to the database and shows success/error alerts.

---
*Get.TechAcad | Module 05 of 12*
