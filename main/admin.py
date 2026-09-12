from django.contrib import admin

from main.models import Certification, Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "category",
        "period",
        "display_order",
    )
    list_filter = ("category",)
    search_fields = ("title", "organization", "description", "skills")
    ordering = ("display_order", "-started_at")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "issuer",
        "category",
        "issued_year",
        "is_featured",
    )
    list_filter = ("category", "issued_year", "is_featured")
    search_fields = ("title", "issuer", "description")
    ordering = ("-is_featured", "-issued_year", "title")
