from django import forms
from .models import ContactMessage, BookingRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Full Name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email Address",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Your Message",
                "rows": 5,
            }),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ["name", "email", "phone", "training_type", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Full Name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email Address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number (optional)",
            }),
            "training_type": forms.Select(attrs={
                "class": "form-select",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Any additional details...",
                "rows": 4,
            }),
        }
