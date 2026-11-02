from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Certification, Experience


class ExperienceSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()
    is_ongoing = serializers.ReadOnlyField()
    skill_list = serializers.ReadOnlyField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "organization",
            "period",
            "display_order",
            "description",
            "category",
            "category_display",
            "thumbnail",
            "started_at",
            "ended_at",
            "is_ongoing",
            "skills",
            "skill_list",
            "star_count",
            "is_starred",
        ]
        read_only_fields = [
            "id",
            "started_at",
            "ended_at",
            "is_ongoing",
            "skill_list",
            "star_count",
            "is_starred",
        ]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Role title cannot be empty."
            )
        return value

    def validate_organization(self, value):
        return strip_tags(value).strip()

    def validate_period(self, value):
        return strip_tags(value).strip()

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Description cannot be empty."
            )
        return value

    def validate_skills(self, value):
        return strip_tags(value).strip()

    def get_category_display(self, obj):
        return obj.get_category_display()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()


class CertificationSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Certification
        fields = [
            "id",
            "title",
            "issuer",
            "category",
            "category_display",
            "issued_year",
            "image_path",
            "credential_url",
            "description",
            "is_featured",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Certification title cannot be empty."
            )
        return value

    def validate_issuer(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Issuing organization cannot be empty."
            )
        return value

    def validate_image_path(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Certificate image path cannot be empty."
            )
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def get_category_display(self, obj):
        return obj.get_category_display()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        usernames = sorted(
            user.username for user in obj.starred_by.all()
        )
        return ", ".join(usernames)
