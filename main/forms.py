from django import forms

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
