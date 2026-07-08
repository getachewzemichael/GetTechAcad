# Module 07 — User Authentication and Authorization
**Duration: 1 Week | Get.TechAcad**

---

## Learning Objectives
- [ ] Implement user registration, login, and logout
- [ ] Use @login_required to protect views
- [ ] Extend User model with a Profile
- [ ] Send password reset emails

---

## 7.1 Built-in Auth URLs
```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',    auth_views.LoginView.as_view(template_name='auth/login.html'),  name='login'),
    path('logout/',   auth_views.LogoutView.as_view(next_page='/'),                   name='logout'),
    path('register/', views.register,                                                  name='register'),
    path('profile/',  views.profile,                                                   name='profile'),
    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
]
```

---

## 7.2 Registration View
```python
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created! Welcome.")
            return redirect('home')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
```

---

## 7.3 Login Template
```html
<!-- templates/auth/login.html -->
{% extends 'base.html' %}
{% block content %}
<h2>Login</h2>
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit" class="btn btn-primary">Login</button>
</form>
<p>No account? <a href="{% url 'register' %}">Register here</a></p>
{% endblock %}
```

---

## 7.4 Protecting Views
```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
```

---

## 7.5 Extended User Profile
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
        return f"{self.user.username} — Profile"

# Auto-create profile when a new user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

---

## 7.6 Accessing Auth Data in Templates
```html
{% if user.is_authenticated %}
  <p>Welcome, {{ user.username }}!</p>
  <a href="{% url 'logout' %}">Logout</a>
{% else %}
  <a href="{% url 'login' %}">Login</a>
  <a href="{% url 'register' %}">Register</a>
{% endif %}
```

---

## 7.7 Settings for Password Reset Email
```python
# settings.py
EMAIL_BACKEND      = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST         = 'smtp.gmail.com'
EMAIL_PORT         = 587
EMAIL_USE_TLS      = True
EMAIL_HOST_USER    = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

## Mini-Project: Full Auth System
Build register, login, logout, profile page, and password reset using Django's built-in auth with a custom user profile model.

---

## Quiz
1. What is `@login_required` used for?
2. What does `request.user` contain?
3. Why do we use signals to create the Profile?
4. What is the difference between `login()` and `authenticate()`?

---
*Get.TechAcad | Module 07 of 12*
