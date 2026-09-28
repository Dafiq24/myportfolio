from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Certification, Experience


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = [
            "title",
            "issuer",
            "category",
            "issued_year",
            "image_path",
            "credential_url",
            "description",
            "is_featured",
        ]
        labels = {
            "title": "Certification title",
            "issuer": "Issuing organization",
            "category": "Category",
            "issued_year": "Year issued",
            "image_path": "Certificate image path",
            "credential_url": "Credential URL",
            "description": "Description",
            "is_featured": "Feature this certification",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Gemini Certified Student"}
            ),
            "issuer": forms.TextInput(
                attrs={"placeholder": "Google for Education"}
            ),
            "category": forms.Select(),
            "issued_year": forms.NumberInput(
                attrs={"min": 1900, "placeholder": "2026"}
            ),
            "image_path": forms.TextInput(
                attrs={
                    "placeholder": "img/certificates/certificate-name.jpg"
                }
            ),
            "credential_url": forms.URLInput(
                attrs={"placeholder": "https://example.com/credential"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe the achievement or learning outcome.",
                    "rows": 4,
                }
            ),
            "is_featured": forms.CheckboxInput(),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError(
                "Certification title cannot contain only HTML tags."
            )
        return title

    def clean_issuer(self):
        issuer = strip_tags(self.cleaned_data["issuer"]).strip()
        if not issuer:
            raise ValidationError(
                "Issuing organization cannot contain only HTML tags."
            )
        return issuer

    def clean_image_path(self):
        image_path = strip_tags(self.cleaned_data["image_path"]).strip()
        if not image_path:
            raise ValidationError(
                "Certificate image path cannot contain only HTML tags."
            )
        return image_path

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "organization",
            "period",
            "display_order",
            "description",
            "category",
            "thumbnail",
            "skills",
        ]
        labels = {
            "title": "Role title",
            "organization": "Organization",
            "period": "Display period",
            "display_order": "Timeline position",
            "description": "Description",
            "category": "Employment type",
            "thumbnail": "Documentation image URL",
            "skills": "Related skills",
        }
        help_texts = {
            "display_order": "Lower numbers appear earlier in the timeline.",
            "thumbnail": "Optional public URL for a documentation image.",
            "skills": "Separate multiple skills with commas.",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Teaching Staff"}
            ),
            "organization": forms.TextInput(
                attrs={"placeholder": "BETIS Fasilkom UI"}
            ),
            "period": forms.TextInput(
                attrs={"placeholder": "January 2026 - June 2026"}
            ),
            "display_order": forms.NumberInput(attrs={"min": 0}),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe your role and contributions.",
                    "rows": 5,
                }
            ),
            "category": forms.Select(),
            "thumbnail": forms.URLInput(
                attrs={"placeholder": "https://example.com/activity.jpg"}
            ),
            "skills": forms.TextInput(
                attrs={"placeholder": "Teaching, Communication, Teamwork"}
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError(
                "Role title cannot contain only HTML tags."
            )
        return title

    def clean_organization(self):
        return strip_tags(self.cleaned_data["organization"]).strip()

    def clean_period(self):
        return strip_tags(self.cleaned_data["period"]).strip()

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError(
                "Description cannot contain only HTML tags."
            )
        return description

    def clean_skills(self):
        return strip_tags(self.cleaned_data["skills"]).strip()
