import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from main.models import Certification, Experience


class CertificationApiTest(TestCase):
    def setUp(self):
        # Keep the API assertions independent from portfolio data migrations.
        Certification.objects.all().delete()

        user_model = get_user_model()
        self.reader = user_model.objects.create_user(
            username="api_reader",
            password="ReaderApiPass!",
        )
        self.other_reader = user_model.objects.create_user(
            username="second_api_reader",
            password="SecondReaderApiPass!",
        )
        self.owner = user_model.objects.create_superuser(
            username="api_owner",
            email="api-owner@example.com",
            password="OwnerApiPass!",
        )

        self.certification = Certification.objects.create(
            title="Django REST Framework Course",
            issuer="PBP Fasilkom UI",
            category="course",
            issued_year=2026,
            image_path="img/certificates/drf-course.png",
            credential_url="https://example.com/drf",
            description="Learning RESTful API design.",
            is_featured=False,
        )
        self.featured_certification = Certification.objects.create(
            title="API Design Achievement",
            issuer="Fasilkom UI",
            category="achievement",
            issued_year=2025,
            image_path="img/certificates/api-achievement.png",
            description="A featured API milestone.",
            is_featured=True,
        )
        self.certification.starred_by.add(self.reader)

        self.list_url = reverse("api:certification-list")
        self.detail_url = reverse(
            "api:certification-detail",
            args=[self.certification.id],
        )
        self.star_url = reverse(
            "api:certification-star",
            args=[self.certification.id],
        )
        self.valid_payload = {
            "title": "REST API Fundamentals",
            "issuer": "PBP Fasilkom UI",
            "category": "course",
            "issued_year": 2026,
            "image_path": "img/certificates/rest-api.png",
            "credential_url": "https://example.com/rest-api",
            "description": "Built with Django REST Framework.",
            "is_featured": False,
        }

    def test_public_list_uses_direct_serializer_contract_and_ordering(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(
            data[0]["id"],
            str(self.featured_certification.id),
        )
        self.assertNotIn("pk", data[0])
        self.assertNotIn("fields", data[0])

        serialized = next(
            item for item in data
            if item["id"] == str(self.certification.id)
        )
        self.assertEqual(serialized["category_display"], "Course")
        self.assertEqual(serialized["star_count"], 1)
        self.assertFalse(serialized["is_starred"])
        self.assertEqual(serialized["starred_by_names"], self.reader.username)

    def test_authenticated_list_reports_the_current_users_star_state(self):
        self.client.force_login(self.reader)
        response = self.client.get(self.list_url)
        serialized = next(
            item for item in response.json()
            if item["id"] == str(self.certification.id)
        )

        self.assertTrue(serialized["is_starred"])
        self.assertEqual(serialized["star_count"], 1)

    def test_title_search_is_case_insensitive(self):
        response = self.client.get(self.list_url, {"title": "dJaNgO"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["title"], self.certification.title)

    def test_public_detail_and_unknown_uuid(self):
        response = self.client.get(self.detail_url)
        missing_url = reverse(
            "api:certification-detail",
            args=[uuid.uuid4()],
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], str(self.certification.id))
        self.assertEqual(self.client.get(missing_url).status_code, 404)

    def test_only_owner_can_create_certifications(self):
        self.assertEqual(
            self.client.post(
                self.list_url,
                self.valid_payload,
                content_type="application/json",
            ).status_code,
            403,
        )

        self.client.force_login(self.reader)
        self.assertEqual(
            self.client.post(
                self.list_url,
                self.valid_payload,
                content_type="application/json",
            ).status_code,
            403,
        )
        self.assertEqual(Certification.objects.count(), 2)

    def test_owner_create_returns_201_and_sanitizes_fields(self):
        self.client.force_login(self.owner)
        payload = {
            **self.valid_payload,
            "title": "<strong>REST API Fundamentals</strong>",
            "description": "<script>alert('x')</script>Safe description",
            "star_count": 999,
            "is_starred": True,
            "starred_by_names": "forged_user",
        }
        response = self.client.post(
            self.list_url,
            payload,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "REST API Fundamentals")
        self.assertEqual(response.json()["description"], "alert('x')Safe description")
        self.assertEqual(response.json()["star_count"], 0)
        self.assertFalse(response.json()["is_starred"])
        self.assertEqual(response.json()["starred_by_names"], "")
        self.assertTrue(
            Certification.objects.filter(title="REST API Fundamentals").exists()
        )

    def test_create_rejects_html_only_required_field(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            self.list_url,
            {**self.valid_payload, "title": "<b></b>"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json())
        self.assertEqual(Certification.objects.count(), 2)

    def test_owner_can_patch_but_regular_user_cannot(self):
        self.client.force_login(self.reader)
        forbidden = self.client.patch(
            self.detail_url,
            {"title": "Reader edit"},
            content_type="application/json",
        )
        self.assertEqual(forbidden.status_code, 403)

        self.client.force_login(self.owner)
        response = self.client.patch(
            self.detail_url,
            {
                "title": "<em>Updated API Course</em>",
                "description": "<b>Updated safely.</b>",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.certification.refresh_from_db()
        self.assertEqual(self.certification.title, "Updated API Course")
        self.assertEqual(self.certification.description, "Updated safely.")

    def test_only_owner_can_delete_and_success_returns_204(self):
        self.client.force_login(self.reader)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertTrue(
            Certification.objects.filter(pk=self.certification.pk).exists()
        )

        self.client.force_login(self.owner)
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        self.assertFalse(
            Certification.objects.filter(pk=self.certification.pk).exists()
        )
        self.assertTrue(
            Certification.objects.filter(
                pk=self.featured_certification.pk,
            ).exists()
        )

    def test_logged_in_user_can_star_and_unstar(self):
        self.client.force_login(self.other_reader)

        starred = self.client.post(self.star_url)
        self.assertEqual(starred.status_code, 200)
        self.assertTrue(starred.json()["is_starred"])
        self.assertEqual(starred.json()["star_count"], 2)

        unstarred = self.client.post(self.star_url)
        self.assertEqual(unstarred.status_code, 200)
        self.assertFalse(unstarred.json()["is_starred"])
        self.assertEqual(unstarred.json()["star_count"], 1)
        self.assertTrue(
            self.certification.starred_by.filter(pk=self.reader.pk).exists()
        )

    def test_star_requires_authentication_and_post(self):
        self.assertEqual(self.client.post(self.star_url).status_code, 403)

        self.client.force_login(self.reader)
        self.assertEqual(self.client.get(self.star_url).status_code, 405)
        self.assertEqual(self.certification.starred_by.count(), 1)

    def test_session_mutations_require_csrf_token(self):
        csrf_client = APIClient(enforce_csrf_checks=True)
        csrf_client.force_login(self.owner)

        create_response = csrf_client.post(
            self.list_url,
            self.valid_payload,
            format="json",
        )
        delete_response = csrf_client.delete(self.detail_url)

        csrf_client.force_login(self.reader)
        star_response = csrf_client.post(self.star_url)

        self.assertEqual(create_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
        self.assertEqual(star_response.status_code, 403)
        self.assertEqual(Certification.objects.count(), 2)
        self.assertEqual(self.certification.starred_by.count(), 1)


class ExperienceApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Keep API assertions independent from portfolio data migrations.
        Experience.objects.all().delete()

        user_model = get_user_model()
        cls.reader_password = "ReaderExperiencePass!"
        cls.editor_password = "EditorExperiencePass!"
        cls.owner_password = "OwnerExperiencePass!"
        cls.reader = user_model.objects.create_user(
            username="experience_reader",
            password=cls.reader_password,
        )
        cls.other_reader = user_model.objects.create_user(
            username="second_experience_reader",
            password="SecondExperiencePass!",
        )
        cls.editor = user_model.objects.create_user(
            username="experience_editor",
            password=cls.editor_password,
        )
        editor_group = Group.objects.create(name="Editor")
        cls.editor.groups.add(editor_group)
        cls.owner = user_model.objects.create_superuser(
            username="experience_owner",
            email="experience-owner@example.com",
            password=cls.owner_password,
        )

        cls.experience = Experience.objects.create(
            title="API Engineering Intern",
            organization="PBP Lab",
            period="March 2026 - Present",
            display_order=2,
            description="Built a role-aware portfolio API.",
            category="internship",
            thumbnail="https://example.com/api-intern.png",
            skills="Django, REST, Testing",
        )
        cls.earlier_experience = Experience.objects.create(
            title="Community Researcher",
            organization="BEM UI",
            period="January 2026 - February 2026",
            display_order=1,
            description="Researched community sustainability programs.",
            category="research",
            skills="Research, Communication",
        )
        cls.experience.starred_by.add(cls.reader)

        cls.list_url = reverse("api:experience-list")
        cls.detail_url = reverse(
            "api:experience-detail",
            args=[cls.experience.id],
        )
        cls.star_url = reverse(
            "api:experience-star",
            args=[cls.experience.id],
        )
        cls.valid_payload = {
            "title": "REST API Teaching Assistant",
            "organization": "Fasilkom UI",
            "period": "August 2026 - Present",
            "display_order": 3,
            "description": "Helped students learn REST API design.",
            "category": "part-time",
            "thumbnail": "https://example.com/rest-ta.png",
            "skills": "Django, Mentoring, API Design",
        }

    def test_public_list_uses_direct_contract_ordering_and_metadata(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], str(self.earlier_experience.id))
        self.assertNotIn("pk", data[0])
        self.assertNotIn("fields", data[0])

        serialized = next(
            item for item in data
            if item["id"] == str(self.experience.id)
        )
        self.assertEqual(serialized["category_display"], "Internship")
        self.assertEqual(serialized["skill_list"], [
            "Django",
            "REST",
            "Testing",
        ])
        self.assertTrue(serialized["is_ongoing"])
        self.assertEqual(serialized["star_count"], 1)
        self.assertFalse(serialized["is_starred"])
        self.assertNotIn("starred_by", serialized)

    def test_list_supports_combined_case_insensitive_filters(self):
        response = self.client.get(
            self.list_url,
            {"q": "bEm", "category": "research"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(
            response.json()[0]["id"],
            str(self.earlier_experience.id),
        )

    def test_public_detail_and_unknown_uuid(self):
        response = self.client.get(self.detail_url)
        missing_url = reverse(
            "api:experience-detail",
            args=[uuid.uuid4()],
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], str(self.experience.id))
        self.assertEqual(self.client.get(missing_url).status_code, 404)

    def test_anonymous_mutations_are_forbidden_without_database_changes(self):
        original_title = self.experience.title
        original_count = Experience.objects.count()

        self.assertEqual(
            self.client.post(self.list_url, self.valid_payload, format="json").status_code,
            403,
        )
        self.assertEqual(
            self.client.patch(
                self.detail_url,
                {"title": "Anonymous edit"},
                format="json",
            ).status_code,
            403,
        )
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(self.client.post(self.star_url).status_code, 403)

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, original_title)
        self.assertEqual(Experience.objects.count(), original_count)
        self.assertEqual(self.experience.starred_by.count(), 1)

    def test_regular_user_can_read_and_star_but_cannot_manage(self):
        self.client.force_login(self.other_reader)
        original_count = Experience.objects.count()

        self.assertEqual(self.client.get(self.list_url).status_code, 200)
        self.assertEqual(
            self.client.post(self.list_url, self.valid_payload, format="json").status_code,
            403,
        )
        self.assertEqual(
            self.client.patch(
                self.detail_url,
                {"title": "Reader edit"},
                format="json",
            ).status_code,
            403,
        )
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

        starred = self.client.post(self.star_url)
        self.assertEqual(starred.status_code, 200)
        self.assertTrue(starred.json()["is_starred"])
        self.assertEqual(starred.json()["star_count"], 2)
        unstarred = self.client.post(self.star_url)
        self.assertEqual(unstarred.status_code, 200)
        self.assertFalse(unstarred.json()["is_starred"])
        self.assertEqual(unstarred.json()["star_count"], 1)

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "API Engineering Intern")
        self.assertEqual(Experience.objects.count(), original_count)
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.reader.pk).exists()
        )

    def test_editor_can_put_patch_and_star_but_cannot_create_or_delete(self):
        self.client.force_login(self.editor)
        original_id = self.experience.id
        original_count = Experience.objects.count()

        self.assertEqual(
            self.client.post(self.list_url, self.valid_payload, format="json").status_code,
            403,
        )
        put_response = self.client.put(
            self.detail_url,
            {
                **self.valid_payload,
                "title": "<strong>Editor Full Update</strong>",
                "star_count": 999,
                "is_starred": True,
            },
            format="json",
        )
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response.json()["title"], "Editor Full Update")
        self.assertEqual(put_response.json()["star_count"], 1)

        patch_response = self.client.patch(
            self.detail_url,
            {"description": "<em>Editor partial update.</em>"},
            format="json",
        )
        self.assertEqual(patch_response.status_code, 200)
        self.assertEqual(
            patch_response.json()["description"],
            "Editor partial update.",
        )
        self.assertEqual(self.client.post(self.star_url).status_code, 200)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.id, original_id)
        self.assertEqual(self.experience.title, "Editor Full Update")
        self.assertEqual(Experience.objects.count(), original_count)
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.reader.pk).exists()
        )
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.editor.pk).exists()
        )

    def test_owner_can_create_and_delete_with_expected_statuses(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            self.list_url,
            {
                **self.valid_payload,
                "title": "<strong>REST API Teaching Assistant</strong>",
                "description": "<script>alert('x')</script>Safe work",
                "star_count": 999,
                "is_starred": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "REST API Teaching Assistant")
        self.assertEqual(response.json()["description"], "alert('x')Safe work")
        self.assertEqual(response.json()["star_count"], 0)
        self.assertFalse(response.json()["is_starred"])

        created_detail_url = reverse(
            "api:experience-detail",
            args=[response.json()["id"]],
        )
        created_star_url = reverse(
            "api:experience-star",
            args=[response.json()["id"]],
        )
        update_response = self.client.patch(
            created_detail_url,
            {"organization": "Updated by owner"},
            format="json",
        )
        star_response = self.client.post(created_star_url)

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(
            update_response.json()["organization"],
            "Updated by owner",
        )
        self.assertEqual(star_response.status_code, 200)
        self.assertTrue(star_response.json()["is_starred"])

        delete_response = self.client.delete(created_detail_url)
        self.assertEqual(delete_response.status_code, 204)
        self.assertEqual(delete_response.content, b"")
        self.assertFalse(
            Experience.objects.filter(pk=response.json()["id"]).exists()
        )
        self.assertTrue(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )

    def test_validation_errors_return_400_without_creating_or_updating(self):
        self.client.force_login(self.owner)
        original_count = Experience.objects.count()
        original_description = self.experience.description

        create_response = self.client.post(
            self.list_url,
            {**self.valid_payload, "title": "<b></b>"},
            format="json",
        )
        patch_response = self.client.patch(
            self.detail_url,
            {"description": "<i></i>"},
            format="json",
        )

        self.assertEqual(create_response.status_code, 400)
        self.assertIn("title", create_response.json())
        self.assertEqual(patch_response.status_code, 400)
        self.assertIn("description", patch_response.json())
        self.assertEqual(Experience.objects.count(), original_count)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.description, original_description)

    def test_unknown_star_target_and_method_restrictions(self):
        self.client.force_login(self.reader)
        missing_star_url = reverse(
            "api:experience-star",
            args=[uuid.uuid4()],
        )

        self.assertEqual(self.client.post(missing_star_url).status_code, 404)
        self.assertEqual(self.client.get(self.star_url).status_code, 405)
        self.assertEqual(
            self.client.put(self.list_url, {}, format="json").status_code,
            403,
        )

        self.client.force_login(self.owner)
        self.assertEqual(
            self.client.put(self.list_url, {}, format="json").status_code,
            405,
        )
        self.assertEqual(self.experience.starred_by.count(), 1)

    def test_session_mutations_enforce_csrf_with_login_and_header(self):
        owner_client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(owner_client.login(
            username=self.owner.username,
            password=self.owner_password,
        ))
        original_count = Experience.objects.count()

        rejected_create = owner_client.post(
            self.list_url,
            self.valid_payload,
            format="json",
        )
        self.assertEqual(rejected_create.status_code, 403)
        self.assertEqual(Experience.objects.count(), original_count)

        owner_client.get(reverse("main:show_experience"))
        owner_token = owner_client.cookies["csrftoken"].value
        accepted_create = owner_client.post(
            self.list_url,
            self.valid_payload,
            format="json",
            HTTP_X_CSRFTOKEN=owner_token,
        )
        self.assertEqual(accepted_create.status_code, 201)

        reader_client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(reader_client.login(
            username=self.reader.username,
            password=self.reader_password,
        ))
        rejected_star = reader_client.post(self.star_url)
        self.assertEqual(rejected_star.status_code, 403)
        self.assertEqual(self.experience.starred_by.count(), 1)

        reader_client.get(reverse("main:show_experience"))
        reader_token = reader_client.cookies["csrftoken"].value
        accepted_star = reader_client.post(
            self.star_url,
            HTTP_X_CSRFTOKEN=reader_token,
        )
        self.assertEqual(accepted_star.status_code, 200)
        self.assertFalse(accepted_star.json()["is_starred"])
        self.assertEqual(accepted_star.json()["star_count"], 0)
