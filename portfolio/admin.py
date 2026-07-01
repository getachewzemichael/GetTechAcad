from django.contrib import admin
from .models import ContactMessage, BookingRequest, ProfilePhoto, CVFile


@admin.register(ProfilePhoto)
class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ["alt_text", "updated_at"]
    readonly_fields = ["updated_at"]


@admin.register(CVFile)
class CVFileAdmin(admin.ModelAdmin):
    list_display = ["label", "updated_at"]
    readonly_fields = ["updated_at"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "email", "subject"]
    readonly_fields = ["created_at"]


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "training_type", "created_at"]
    list_filter = ["training_type", "created_at"]
    search_fields = ["name", "email"]
    readonly_fields = ["created_at"]
