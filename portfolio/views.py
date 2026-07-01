from django.shortcuts import render, redirect
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
