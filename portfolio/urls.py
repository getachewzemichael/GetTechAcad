from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("experience/", views.experience, name="experience"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("certifications/", views.certifications, name="certifications"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("book-training/", views.book_training, name="book_training"),
    path("download-cv/", views.download_cv, name="download_cv"),
]
