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


def download_cv(request):
    """
    Redirect to Cloudinary with fl_attachment injected into the URL
    so the browser downloads the PDF directly from Cloudinary's CDN.
    """
    cv = CVFile.objects.first()
    if not cv:
        raise Http404("CV not available.")

    # Get the base URL and force https
    base_url = cv.cv_file.url.replace("http://", "https://")

    # Inject fl_attachment into the Cloudinary URL
    # From: https://res.cloudinary.com/xxx/raw/upload/v.../cv/filename
    # To:   https://res.cloudinary.com/xxx/raw/upload/fl_attachment:CV_Name/v.../cv/filename
    download_url = base_url.replace(
        "/raw/upload/",
        "/raw/upload/fl_attachment:Getachew_Zemicheal_Hadgu_CV/"
    )

    return HttpResponseRedirect(download_url)
