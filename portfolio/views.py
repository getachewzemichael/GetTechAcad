from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm, BookingForm
from .models import ProfilePhoto, CVFile


def _get_profile_photo():
    return ProfilePhoto.objects.first()


def _get_cv():
    return CVFile.objects.first()


def home(request):
    return render(request, "portfolio/home.html", {
        "profile_photo": _get_profile_photo(),
        "cv": _get_cv(),
    })


def about(request):
    return render(request, "portfolio/about.html", {
        "profile_photo": _get_profile_photo(),
        "cv": _get_cv(),
    })


def experience(request):
    return render(request, "portfolio/experience.html")


def skills(request):
    return render(request, "portfolio/skills.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def certifications(request):
    return render(request, "portfolio/certifications.html")


def services(request):
    return render(request, "portfolio/services.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect("contact")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact.html", {"form": form})


def book_training(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking request submitted! I'll get back to you shortly.")
            return redirect("book_training")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()
    return render(request, "portfolio/book_training.html", {"form": form})


def debug_media(request):
    """Temporary debug view - remove after fixing."""
    cv = CVFile.objects.first()
    photo = ProfilePhoto.objects.first()
    return JsonResponse({
        "cv_exists": cv is not None,
        "cv_field_value": str(cv.cv_file) if cv else None,
        "cv_url": cv.cv_file.url if cv else None,
        "photo_exists": photo is not None,
        "photo_field_value": str(photo.photo) if photo else None,
        "photo_url": photo.photo.url if photo else None,
    })


def course_django(request):
    modules = [
        {"number": "00", "title": "Setup & Orientation",          "duration": "Day 1"},
        {"number": "01", "title": "Python Fundamentals",           "duration": "2 Weeks"},
        {"number": "02", "title": "HTML, CSS & Bootstrap 5",       "duration": "1 Week"},
        {"number": "03", "title": "Introduction to Django",        "duration": "1 Week"},
        {"number": "04", "title": "Models & Database ORM",         "duration": "1.5 Weeks"},
        {"number": "05", "title": "Forms & Validation",            "duration": "1 Week"},
        {"number": "06", "title": "Django Admin Panel",            "duration": "3 Days"},
        {"number": "07", "title": "User Authentication",           "duration": "1 Week"},
        {"number": "08", "title": "Class-Based Views",             "duration": "4 Days"},
        {"number": "09", "title": "Django REST Framework",         "duration": "1.5 Weeks"},
        {"number": "10", "title": "Frontend Integration & AJAX",   "duration": "1 Week"},
        {"number": "11", "title": "Deployment to Production",      "duration": "4 Days"},
        {"number": "12", "title": "Capstone Project",              "duration": "2 Weeks"},
    ]
    return render(request, "portfolio/course_django.html", {"modules": modules})


def download_course_guide(request):
    """Serve the Django course guide as a download."""
    import os
    from django.conf import settings as django_settings
    from django.http import FileResponse, Http404

    guide_path = os.path.join(django_settings.BASE_DIR, "static", "cv", "Django-Course-Guide.md")
    if not os.path.exists(guide_path):
        raise Http404("Course guide not available.")
    response = FileResponse(
        open(guide_path, "rb"),
        content_type="text/markdown"
    )
    response["Content-Disposition"] = 'attachment; filename="Get.TechAcad-Django-Course-Guide.md"'
    return response


def download_cv(request):
    """
    Serve CV directly from static files - reliable, no auth issues.
    Falls back to Cloudinary if static file not found.
    """
    import os
    from django.conf import settings as django_settings
    from django.http import FileResponse

    # Try static file first (committed to repo, always works)
    static_cv_path = os.path.join(django_settings.BASE_DIR, "static", "cv", "Getachew_Zemicheal_Hadgu_CV.pdf")
    if os.path.exists(static_cv_path):
        response = FileResponse(
            open(static_cv_path, "rb"),
            content_type="application/pdf"
        )
        response["Content-Disposition"] = 'attachment; filename="Getachew_Zemicheal_Hadgu_CV.pdf"'
        return response

    # Fallback: redirect to Cloudinary
    cv = CVFile.objects.first()
    if not cv:
        raise Http404("CV not available.")
    base_url = cv.cv_file.url.replace("http://", "https://")
    download_url = base_url.replace(
        "/raw/upload/",
        "/raw/upload/fl_attachment:Getachew_Zemicheal_Hadgu_CV/"
    )
    return HttpResponseRedirect(download_url)
