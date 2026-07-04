import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
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
    from django.http import JsonResponse
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
    cv = CVFile.objects.first()
    if not cv:
        raise Http404("CV not available.")
    try:
        response = requests.get(cv.cv_file.url, timeout=15)
        response.raise_for_status()
    except Exception:
        raise Http404("CV could not be fetched.")
    http_response = HttpResponse(response.content, content_type="application/pdf")
    http_response["Content-Disposition"] = 'attachment; filename="Getachew_Zemicheal_Hadgu_CV.pdf"'
    return http_response
