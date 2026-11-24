from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from main.models import Project


class Tutorial10ConfigurationTest(TestCase):
    def test_token_authentication_and_cors_are_configured(self):
        self.assertIn("corsheaders", settings.INSTALLED_APPS)
        self.assertIn("rest_framework.authtoken", settings.INSTALLED_APPS)
        self.assertIn(
            "rest_framework.authentication.TokenAuthentication",
            settings.REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"],
        )
        self.assertLess(
            settings.MIDDLEWARE.index(
                "corsheaders.middleware.CorsMiddleware"
            ),
            settings.MIDDLEWARE.index(
                "django.middleware.common.CommonMiddleware"
            ),
        )


class ProjectTokenApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()
        cls.owner_password = "OwnerProjectPass!"
        cls.owner = user_model.objects.create_superuser(
            username="project_owner",
            email="project-owner@example.com",
            password=cls.owner_password,
        )
        cls.reader = user_model.objects.create_user(
            username="project_reader",
            password="ReaderProjectPass!",
        )
        cls.project = Project.objects.create(
            title="MyPortfolio Web",
            description="A Django portfolio application.",
            tech_stack="Django, PostgreSQL, JavaScript",
            project_url="https://example.com/portfolio",
            project_image_url="https://example.com/portfolio.png",
        )

    def setUp(self):
        self.list_url = reverse("api:project-list")
        self.detail_url = reverse(
            "api:project-detail",
            args=[self.project.id],
        )
        self.token_url = reverse("api:api-token-auth")
        self.logout_url = reverse("api:api-logout")
        self.valid_payload = {
            "title": "MyPortfolio Mobile",
            "description": "A Flutter client for the portfolio API.",
            "tech_stack": "Flutter, Django REST Framework",
            "project_url": "https://example.com/mobile",
            "project_image_url": "",
        }

    def _obtain_owner_token(self):
        response = self.client.post(
            self.token_url,
            {
                "username": self.owner.username,
                "password": self.owner_password,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())
        return response.json()["token"]

    def test_project_list_and_detail_are_public(self):
        list_response = self.client.get(self.list_url)
        detail_response = self.client.get(self.detail_url)

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.json()), 1)
        self.assertEqual(
            list_response.json()[0]["id"],
            str(self.project.id),
        )
        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(
            detail_response.json()["tech_stack"],
            self.project.tech_stack,
        )

    def test_anonymous_and_regular_user_cannot_create_project(self):
        anonymous_response = self.client.post(
            self.list_url,
            self.valid_payload,
            format="json",
        )
        reader_token = Token.objects.create(user=self.reader)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {reader_token.key}"
        )
        reader_response = self.client.post(
            self.list_url,
            self.valid_payload,
            format="json",
        )

        self.assertEqual(anonymous_response.status_code, 403)
        self.assertEqual(reader_response.status_code, 403)
        self.assertEqual(Project.objects.count(), 1)

    def test_owner_token_creates_project_and_sanitizes_text(self):
        token = self._obtain_owner_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = self.client.post(
            self.list_url,
            {
                **self.valid_payload,
                "title": "<strong>MyPortfolio Mobile</strong>",
                "description": "<script>alert('x')</script>Safe project",
                "tech_stack": "<em>Flutter, Django</em>",
                "id": "00000000-0000-0000-0000-000000000000",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "MyPortfolio Mobile")
        self.assertEqual(
            response.json()["description"],
            "alert('x')Safe project",
        )
        self.assertEqual(response.json()["tech_stack"], "Flutter, Django")
        self.assertNotEqual(
            response.json()["id"],
            "00000000-0000-0000-0000-000000000000",
        )

    def test_logout_revokes_current_token(self):
        token = self._obtain_owner_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        response = self.client.post(self.logout_url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        self.assertFalse(Token.objects.filter(key=token).exists())
        self.assertEqual(self.client.post(self.logout_url).status_code, 401)

    def test_session_authentication_remains_available(self):
        session_client = APIClient()
        session_client.force_login(self.owner)

        response = session_client.post(
            self.list_url,
            self.valid_payload,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
