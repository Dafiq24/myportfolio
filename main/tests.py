import uuid

from django.contrib import admin
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from main.forms import CertificationForm
from main.models import Certification, Experience


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="HR Software Engineering Academy",
            organization="COMPFEST 18",
            period="March 2026 - Present",
            description=(
                "Supported staff recruitment communications and coordinated "
                "administrative screening, interviews, and onboarding."
            ),
            category="volunteer",
            skills="Recruitment, Coordination, Communication",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"',
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(
            str(self.experience),
            "HR Software Engineering Academy",
        )
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, self.experience.organization)
        self.assertContains(response, self.experience.period)
        self.assertContains(response, "Recruitment")
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"',
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(
            response,
            "No experiences have been added yet.",
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, self.experience.title)


class CertificationTest(TestCase):
    def setUp(self):
        Certification.objects.all().delete()
        self.certification = Certification.objects.create(
            title="Gemini Certified Student",
            issuer="Google for Education",
            category="certification",
            issued_year=2026,
            image_path="img/certificates/gemini-certified-student.jpg",
            description="Recognition of foundational knowledge in generative AI.",
        )

    def test_certification_model(self):
        self.assertEqual(str(self.certification), "Gemini Certified Student")
        self.assertEqual(
            self.certification.get_category_display(),
            "Certification",
        )

    def test_certifications_page_uses_model_data(self):
        response = self.client.get(reverse("main:show_certifications"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certifications.html")
        self.assertContains(response, self.certification.title)
        self.assertContains(response, self.certification.issuer)
        self.assertContains(response, str(self.certification.issued_year))
        self.assertContains(
            response,
            f'id="certificate-{self.certification.id}"',
        )

    def test_empty_certifications_page(self):
        Certification.objects.all().delete()
        response = self.client.get(reverse("main:show_certifications"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No certifications have been added yet.",
        )

    def test_featured_certification_is_ordered_first(self):
        featured = Certification.objects.create(
            title="Finalist - ShARE Global Case Summit",
            issuer="ShARE ITB, DWDG UGM & ShARE UB",
            category="achievement",
            issued_year=2026,
            image_path="img/certificates/sgcs-finalist.jpg",
            is_featured=True,
        )

        certification_list = list(Certification.objects.all())

        self.assertEqual(certification_list[0], featured)

    def test_navigation_uses_named_certifications_url(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(
            response,
            f'href="{reverse("main:show_certifications")}"',
        )

    def test_certification_detail_page(self):
        detail_url = reverse(
            "main:show_certification_detail",
            kwargs={"certification_id": self.certification.id},
        )
        delete_url = reverse(
            "main:delete_certification",
            kwargs={"certification_id": self.certification.id},
        )
        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification_detail.html")
        self.assertEqual(response.context["certification"], self.certification)
        self.assertContains(response, self.certification.title)
        self.assertContains(response, self.certification.issuer)
        self.assertContains(response, self.certification.description)
        self.assertContains(response, f'action="{delete_url}"')
        self.assertContains(response, 'name="csrfmiddlewaretoken"')

    def test_certifications_page_links_to_detail(self):
        detail_url = reverse(
            "main:show_certification_detail",
            kwargs={"certification_id": self.certification.id},
        )
        response = self.client.get(reverse("main:show_certifications"))

        self.assertContains(response, f'href="{detail_url}"')

    def test_unknown_certification_detail_returns_404(self):
        response = self.client.get(
            reverse(
                "main:show_certification_detail",
                kwargs={"certification_id": uuid.uuid4()},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_portfolio_models_are_registered_in_admin(self):
        self.assertTrue(admin.site.is_registered(Experience))
        self.assertTrue(admin.site.is_registered(Certification))

    def test_certification_form_exposes_expected_fields(self):
        form = CertificationForm()

        self.assertEqual(
            list(form.fields),
            [
                "title",
                "issuer",
                "category",
                "issued_year",
                "image_path",
                "credential_url",
                "description",
                "is_featured",
            ],
        )
        self.assertNotIn("id", form.fields)

    def test_create_certification_page_contains_form_and_csrf_token(self):
        response = self.client.get(reverse("main:create_certification"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification_form.html")
        self.assertIsInstance(response.context["form"], CertificationForm)
        self.assertContains(response, 'name="csrfmiddlewaretoken"')

    def test_valid_certification_submission_creates_object(self):
        response = self.client.post(
            reverse("main:create_certification"),
            {
                "title": "Java Collections Framework",
                "issuer": "Udemy",
                "category": "course",
                "issued_year": 2026,
                "image_path": "img/certificates/java-collections.png",
                "credential_url": "",
                "description": "Studied the Java Collections Framework.",
            },
        )

        self.assertRedirects(response, reverse("main:show_certifications"))
        self.assertTrue(
            Certification.objects.filter(
                title="Java Collections Framework"
            ).exists()
        )

    def test_invalid_certification_submission_shows_errors(self):
        response = self.client.post(
            reverse("main:create_certification"),
            {
                "title": "",
                "issuer": "Udemy",
                "category": "course",
                "issued_year": 2026,
                "image_path": "img/certificates/java-collections.png",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"],
            "title",
            "This field is required.",
        )
        self.assertEqual(Certification.objects.count(), 1)

    def test_certifications_json_endpoint_returns_model_data(self):
        response = self.client.get(reverse("main:get_certifications_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        payload = response.json()
        self.assertEqual(len(payload), 1)
        self.assertEqual(
            payload[0]["fields"]["title"],
            self.certification.title,
        )

    def test_certifications_json_filter_is_case_insensitive(self):
        Certification.objects.create(
            title="Java Collections Framework",
            issuer="Udemy",
            category="course",
            issued_year=2026,
            image_path="img/certificates/java-collections.png",
        )

        response = self.client.get(
            reverse("main:get_certifications_json"),
            {"title": "gEmInI"},
        )
        payload = response.json()

        self.assertEqual(len(payload), 1)
        self.assertEqual(
            payload[0]["fields"]["title"],
            self.certification.title,
        )

    def test_certifications_page_filters_deserialized_data(self):
        other_certification = Certification.objects.create(
            title="Java Collections Framework",
            issuer="Udemy",
            category="course",
            issued_year=2026,
            image_path="img/certificates/java-collections.png",
        )

        response = self.client.get(
            reverse("main:show_certifications"),
            {"title": "Gemini"},
        )

        self.assertContains(response, self.certification.title)
        self.assertNotContains(response, other_certification.title)
        self.assertContains(response, "certificate-track-static")
        self.assertNotContains(
            response,
            '<div class="certificate-set" aria-hidden="true">',
        )

    def test_certification_search_has_contextual_empty_state(self):
        response = self.client.get(
            reverse("main:show_certifications"),
            {"title": "Unknown credential"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No certifications match",
        )
        self.assertContains(response, "Unknown credential")

    def test_delete_certification_rejects_get_requests(self):
        delete_url = reverse(
            "main:delete_certification",
            kwargs={"certification_id": self.certification.id},
        )

        response = self.client.get(delete_url)

        self.assertEqual(response.status_code, 405)
        self.assertTrue(
            Certification.objects.filter(pk=self.certification.id).exists()
        )

    def test_delete_certification_requires_csrf_token(self):
        csrf_client = Client(enforce_csrf_checks=True)
        delete_url = reverse(
            "main:delete_certification",
            kwargs={"certification_id": self.certification.id},
        )

        response = csrf_client.post(delete_url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Certification.objects.filter(pk=self.certification.id).exists()
        )

    def test_delete_certification_removes_object(self):
        delete_url = reverse(
            "main:delete_certification",
            kwargs={"certification_id": self.certification.id},
        )

        response = self.client.post(delete_url)

        self.assertRedirects(response, reverse("main:show_certifications"))
        self.assertFalse(
            Certification.objects.filter(pk=self.certification.id).exists()
        )

    def test_unknown_certification_delete_returns_404(self):
        response = self.client.post(
            reverse(
                "main:delete_certification",
                kwargs={"certification_id": uuid.uuid4()},
            )
        )

        self.assertEqual(response.status_code, 404)
