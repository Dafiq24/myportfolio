from django import forms

from main.models import Certification


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
