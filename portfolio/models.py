from django.db import models
from cloudinary.models import CloudinaryField


class ProfilePhoto(models.Model):
    """Single profile photo used on the home and about pages."""
    photo = CloudinaryField("Profile Photo", folder="profile")
    alt_text = models.CharField(max_length=150, default="Getachew Zemicheal Hadgu")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile Photo"
        verbose_name_plural = "Profile Photo"

    def __str__(self):
        return "Profile Photo"

    def save(self, *args, **kwargs):
        if not self.pk and ProfilePhoto.objects.exists():
            ProfilePhoto.objects.all().delete()
        super().save(*args, **kwargs)


class CVFile(models.Model):
    """Uploadable CV/resume file served as a download across the site."""
    cv_file = CloudinaryField("CV File (PDF)", folder="cv", resource_type="raw", type="upload")
    label = models.CharField(max_length=100, default="Getachew Zemicheal Hadgu - CV")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CV File"
        verbose_name_plural = "CV File"

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        # Only one CV at a time
        if not self.pk and CVFile.objects.exists():
            CVFile.objects.all().delete()
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ["-created_at"]


class BookingRequest(models.Model):
    TRAINING_CHOICES = [
        ("basic_computer", "Basic Computer Skills"),
        ("Python-Django Full Course", "Python-Django Full Stack Web Development"),
        ("Ai Full Course with Prompt Engineering", "AI Full Course From Prompt Engineering to Practical AI Workflows"),
        ("digital_marketing", "Digital Marketing Full Course"),
        ("SMMA", "Social Media Marketing Agency (SMMA)"),
        ("Video Editing", "Video Editing With CapCut"),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    training_type = models.CharField(max_length=60, choices=TRAINING_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_training_type_display()}"

    class Meta:
        ordering = ["-created_at"]
