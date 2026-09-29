import uuid

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from main.forms import CertificationForm, ExperienceForm
from main.models import Certification, Experience


class AuthenticationWorkflowTest(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.password = "SecureTutorial4Pass!"
        self.user = self.user_model.objects.create_user(
            username="portfolio_reader",
            password=self.password,
        )
        self.register_url = reverse("main:register")
        self.login_url = reverse("main:login")
        self.logout_url = reverse("main:logout")

    def test_anonymous_navbar_shows_login_and_register(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertContains(response, f'href="{self.login_url}"')
        self.assertContains(response, f'href="{self.register_url}"')
        self.assertNotContains(response, f'href="{self.logout_url}"')

    def test_register_page_uses_builtin_fields_and_csrf(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password1"')
        self.assertContains(response, 'name="password2"')
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_valid_registration_hashes_password_and_redirects(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "new_reader",
                "password1": self.password,
                "password2": self.password,
            },
            follow=True,
        )
        self.assertRedirects(response, self.login_url)
        new_user = self.user_model.objects.get(username="new_reader")
        self.assertTrue(new_user.check_password(self.password))
        self.assertNotEqual(new_user.password, self.password)
        self.assertContains(response, "Account created successfully")

    def test_invalid_registration_does_not_create_user(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "new_reader",
                "password1": self.password,
                "password2": "DifferentPassword!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            self.user_model.objects.filter(username="new_reader").exists()
        )
        self.assertContains(response, "didn’t match")

    def test_login_rejects_invalid_credentials(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user.username, "password": "wrong-password"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertContains(response, "correct username and password")

    def test_login_creates_session_and_authenticated_navbar(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user.username, "password": self.password},
            follow=True,
        )
        self.assertRedirects(response, reverse("main:show_main"))
        self.assertEqual(
            int(self.client.session["_auth_user_id"]), self.user.pk
        )
        self.assertContains(response, self.user.username)
        self.assertContains(response, f'href="{self.logout_url}"')
        self.assertNotContains(response, f'href="{self.register_url}"')

    def test_login_continues_to_a_safe_local_destination(self):
        destination = reverse("main:show_experience")
        login_page = self.client.get(self.login_url, {"next": destination})
        self.assertContains(
            login_page,
            f'<input type="hidden" name="next" value="{destination}">',
            html=True,
        )

        response = self.client.post(
            self.login_url,
            {
                "username": self.user.username,
                "password": self.password,
                "next": destination,
            },
        )
        self.assertRedirects(
            response,
            destination,
            fetch_redirect_response=False,
        )

    def test_login_ignores_unsafe_external_destinations(self):
        for destination in (
            "https://malicious.example/collect",
            "//malicious.example/collect",
        ):
            with self.subTest(destination=destination):
                self.client.logout()
                response = self.client.post(
                    self.login_url,
                    {
                        "username": self.user.username,
                        "password": self.password,
                        "next": destination,
                    },
                )
                self.assertRedirects(
                    response,
                    reverse("main:show_main"),
                    fetch_redirect_response=False,
                )

    def test_invalid_login_preserves_a_safe_destination(self):
        destination = reverse("main:show_experience")
        response = self.client.post(
            self.login_url,
            {
                "username": self.user.username,
                "password": "wrong-password",
                "next": destination,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'value="{destination}"')
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_successful_login_sets_hardened_last_login_cookie(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user.username, "password": self.password},
        )
        cookie = response.cookies["last_login"]
        self.assertRegex(
            cookie.value,
            r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$",
        )
        self.assertTrue(cookie["httponly"])
        self.assertEqual(cookie["samesite"], "Lax")

    def test_failed_login_does_not_set_last_login_cookie(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user.username, "password": "wrong-password"},
        )
        self.assertNotIn("last_login", response.cookies)

    def test_profile_reads_last_login_cookie_with_safe_default(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertContains(
            response,
            "No login session has been recorded in this browser.",
        )
        self.client.cookies["last_login"] = "2026-09-21 12:34:56 UTC"
        response = self.client.get(reverse("main:show_main"))
        self.assertContains(response, "2026-09-21 12:34:56 UTC")

    def test_logout_clears_authentication_without_deleting_account(self):
        self.client.login(username=self.user.username, password=self.password)
        self.client.cookies["last_login"] = "2026-09-21 12:34:56 UTC"
        response = self.client.get(self.logout_url)
        self.assertRedirects(
            response,
            reverse("main:show_main"),
            fetch_redirect_response=False,
        )
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertTrue(
            self.user_model.objects.filter(pk=self.user.pk).exists()
        )
        self.assertEqual(response.cookies["last_login"]["max-age"], 0)
        profile_response = self.client.get(reverse("main:show_main"))
        self.assertContains(profile_response, f'href="{self.login_url}"')

    def test_authentication_forms_require_csrf_token(self):
        csrf_client = Client(enforce_csrf_checks=True)
        for url, data in (
            (
                self.register_url,
                {
                    "username": "csrf_user",
                    "password1": self.password,
                    "password2": self.password,
                },
            ),
            (
                self.login_url,
                {"username": self.user.username, "password": self.password},
            ),
        ):
            with self.subTest(url=url):
                self.assertEqual(csrf_client.post(url, data).status_code, 403)


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
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, 'id="experience-loading"')
        self.assertContains(response, 'id="experience-error"')
        self.assertContains(response, 'id="experience-empty"')
        self.assertContains(response, 'id="experience-timeline"')
        self.assertContains(response, reverse("main:get_experiences_json"))
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

        response = self.client.get(reverse("main:get_experiences_json"))

        self.assertFalse(self.experience.is_ongoing)
        fields = response.json()[0]["fields"]
        self.assertFalse(fields["is_ongoing"])
        self.assertIsNotNone(fields["ended_at"])


class ExperienceWorkflowTest(TestCase):
    def setUp(self):
        # Isolate assertions from portfolio records created by data migrations.
        Experience.objects.all().delete()
        self.data = {
            "title": "Student Welfare Intern",
            "organization": "BEM Fasilkom UI",
            "period": "September 2025 - December 2025",
            "display_order": 4,
            "description": "Coordinated student advocacy activities.",
            "category": "internship",
            "thumbnail": "https://example.com/activity.jpg",
            "skills": "Advocacy, Communication, Teamwork",
        }
        self.experience = Experience.objects.create(**self.data)
        user_model = get_user_model()
        self.regular_user = user_model.objects.create_user(
            username="experience_reader",
            password="ReaderTugas4Pass!",
        )
        self.other_user = user_model.objects.create_user(
            username="second_reader",
            password="SecondTugas4Pass!",
        )
        self.editor = user_model.objects.create_user(
            username="experience_editor",
            password="EditorTugas4Pass!",
        )
        self.editor_group = Group.objects.create(name="Editor")
        self.editor.groups.add(self.editor_group)
        self.owner = user_model.objects.create_superuser(
            username="portfolio_owner_tugas4",
            email="owner-tugas4@example.com",
            password="OwnerTugas4Pass!",
        )
        self.list_url = reverse("main:show_experience")
        self.create_url = reverse("main:create_experience")
        self.ajax_create_url = reverse("main:create_experience_ajax")
        self.json_url = reverse("main:get_experiences_json")
        self.update_url = reverse(
            "main:update_experience", args=[self.experience.pk]
        )
        self.delete_url = reverse(
            "main:delete_experience", args=[self.experience.pk]
        )
        self.star_url = reverse(
            "main:toggle_experience_star", args=[self.experience.pk]
        )

    def test_form_exposes_all_editable_portfolio_fields(self):
        self.assertEqual(list(ExperienceForm().fields), list(self.data))

    def test_optional_fields_can_be_empty(self):
        data = {**self.data, "organization": "", "period": "",
                "thumbnail": "", "skills": ""}
        self.assertTrue(ExperienceForm(data).is_valid())

    def test_form_rejects_invalid_category_order_and_thumbnail(self):
        for field, value in (
            ("category", "unknown"),
            ("display_order", -1),
            ("thumbnail", "not-a-url"),
        ):
            with self.subTest(field=field):
                form = ExperienceForm({**self.data, field: value})
                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)

    def test_form_strips_html_from_experience_text_fields(self):
        form = ExperienceForm(
            {
                **self.data,
                "title": "<strong>Student Welfare Intern</strong>",
                "organization": "<em>BEM Fasilkom UI</em>",
                "period": "<span>September - December 2025</span>",
                "description": "<b>Coordinated</b> student advocacy.",
                "skills": "<i>Advocacy</i>, Communication",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["title"], "Student Welfare Intern")
        self.assertEqual(form.cleaned_data["organization"], "BEM Fasilkom UI")
        self.assertEqual(
            form.cleaned_data["period"],
            "September - December 2025",
        )
        self.assertEqual(
            form.cleaned_data["description"],
            "Coordinated student advocacy.",
        )
        self.assertEqual(
            form.cleaned_data["skills"],
            "Advocacy, Communication",
        )

    def test_form_rejects_required_text_containing_only_html_tags(self):
        for field in ("title", "description"):
            with self.subTest(field=field):
                form = ExperienceForm({**self.data, field: "<strong></strong>"})
                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)

    def test_form_rejects_img_onerror_xss_payload_in_required_text(self):
        payload = '<img src="x" onerror="alert(\'XSS!\')">'

        for field in ("title", "description"):
            with self.subTest(field=field):
                form = ExperienceForm({**self.data, field: payload})
                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)

    def test_create_page_uses_shared_template_and_csrf(self):
        self.client.force_login(self.owner)
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "csrfmiddlewaretoken")
        self.assertContains(response, "Add experience")

    def test_valid_create_saves_all_fields_and_success_feedback(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            self.create_url, {**self.data, "title": "Teaching Staff"}, follow=True
        )
        self.assertRedirects(response, self.list_url)
        created = Experience.objects.get(title="Teaching Staff")
        for field, value in self.data.items():
            if field != "title":
                self.assertEqual(getattr(created, field), value)
        self.assertEqual(Experience.objects.count(), 2)
        self.assertContains(response, "Experience added successfully.")
        self.assertContains(response, "Dismiss notification")

    def test_ajax_create_rejects_get(self):
        self.client.force_login(self.owner)

        self.assertEqual(self.client.get(self.ajax_create_url).status_code, 405)

    def test_ajax_create_returns_json_403_for_non_owner(self):
        anonymous_response = self.client.post(self.ajax_create_url, {})
        self.assertEqual(anonymous_response.status_code, 403)
        self.assertEqual(
            anonymous_response["Content-Type"],
            "application/json",
        )

        self.client.force_login(self.regular_user)
        regular_response = self.client.post(self.ajax_create_url, {})
        self.assertEqual(regular_response.status_code, 403)
        self.assertIn("message", regular_response.json())

    def test_ajax_create_returns_field_validation_errors(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            self.ajax_create_url,
            {**self.data, "title": ""},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])
        self.assertEqual(Experience.objects.count(), 1)

    def test_ajax_create_returns_201_and_saves_cleaned_experience(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            self.ajax_create_url,
            {
                **self.data,
                "title": "<strong>AJAX Experience</strong>",
                "description": "Created <em>without</em> a reload.",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("pk", response.json())
        created = Experience.objects.get(title="AJAX Experience")
        self.assertEqual(created.description, "Created without a reload.")

    def test_ajax_create_requires_csrf_token(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.owner)
        response = csrf_client.post(self.ajax_create_url, self.data)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    def test_invalid_create_preserves_count_and_input(self):
        self.client.force_login(self.owner)
        response = self.client.post(self.create_url, {**self.data, "title": ""})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context["form"], "title", "This field is required.")
        self.assertEqual(Experience.objects.count(), 1)
        self.assertContains(response, self.experience.organization)

    def test_update_page_prefills_every_field(self):
        self.client.force_login(self.editor)
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")
        self.assertContains(response, "Save changes")
        form = response.context["form"]
        self.assertEqual(form.instance.pk, self.experience.pk)
        for field, value in self.data.items():
            self.assertEqual(form.initial[field], value)

    def test_update_changes_same_object_without_duplicates(self):
        self.client.force_login(self.editor)
        original_pk = self.experience.pk
        original_started_at = self.experience.started_at
        response = self.client.post(
            self.update_url,
            {**self.data, "title": "Updated Role", "skills": "Django, Testing"},
            follow=True,
        )
        self.assertRedirects(response, self.list_url)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.pk, original_pk)
        self.assertEqual(self.experience.started_at, original_started_at)
        self.assertEqual(self.experience.title, "Updated Role")
        self.assertEqual(self.experience.skill_list, ["Django", "Testing"])
        self.assertEqual(Experience.objects.count(), 1)
        self.assertContains(response, "Experience updated successfully.")

    def test_invalid_update_does_not_modify_database(self):
        self.client.force_login(self.editor)
        response = self.client.post(self.update_url, {**self.data, "title": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", response.context["form"].errors)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, self.data["title"])
        self.assertEqual(Experience.objects.count(), 1)

    def test_unknown_update_returns_404_for_get_and_post(self):
        self.client.force_login(self.editor)
        url = reverse("main:update_experience", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(self.client.post(url, self.data).status_code, 404)

    def test_mutations_require_csrf_tokens(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.owner)
        for url in (self.create_url, self.update_url, self.delete_url):
            with self.subTest(url=url):
                self.assertEqual(client.post(url, self.data).status_code, 403)
        self.experience.refresh_from_db()
        self.assertEqual(Experience.objects.count(), 1)
        self.assertEqual(self.experience.title, self.data["title"])

    def test_delete_rejects_non_post_methods(self):
        self.client.force_login(self.owner)
        for method in ("get", "put", "patch", "delete", "head"):
            with self.subTest(method=method):
                response = getattr(self.client, method)(self.delete_url)
                self.assertEqual(response.status_code, 405)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_delete_with_valid_csrf_removes_only_target(self):
        other = Experience.objects.create(**{**self.data, "title": "Keep this role"})
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.owner)
        client.get(self.list_url)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.delete_url, {"csrfmiddlewaretoken": token}, follow=True
        )
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Experience.objects.filter(pk=self.experience.pk).exists())
        self.assertTrue(Experience.objects.filter(pk=other.pk).exists())
        self.assertContains(response, "deleted successfully.")

    def test_unknown_delete_returns_404(self):
        self.client.force_login(self.owner)
        url = reverse("main:delete_experience", args=[uuid.uuid4()])
        self.assertEqual(self.client.post(url).status_code, 404)
        self.assertEqual(Experience.objects.count(), 1)

    def test_anonymous_crud_requests_redirect_to_login(self):
        requests = (
            ("get", self.create_url, None),
            ("get", self.update_url, None),
            ("post", self.delete_url, {}),
        )
        for method, url, data in requests:
            with self.subTest(method=method, url=url):
                response = getattr(self.client, method)(url, data=data)
                self.assertRedirects(
                    response,
                    f"{reverse('main:login')}?next={url}",
                    fetch_redirect_response=False,
                )

    def test_regular_user_receives_403_for_all_crud_operations(self):
        self.client.force_login(self.regular_user)
        self.assertEqual(self.client.get(self.create_url).status_code, 403)
        self.assertEqual(self.client.get(self.update_url).status_code, 403)
        self.assertEqual(self.client.post(self.delete_url).status_code, 403)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_forbidden_response_uses_helpful_custom_page(self):
        self.client.force_login(self.regular_user)
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, "403.html")
        self.assertContains(
            response,
            "This action is outside your access level.",
            status_code=403,
        )
        self.assertContains(
            response,
            self.regular_user.username,
            status_code=403,
        )
        self.assertContains(
            response,
            f'href="{self.list_url}"',
            status_code=403,
        )

    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.client.force_login(self.editor)
        self.assertEqual(self.client.get(self.update_url).status_code, 200)
        self.assertEqual(self.client.get(self.create_url).status_code, 403)
        self.assertEqual(self.client.post(self.delete_url).status_code, 403)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_crud_controls_follow_the_role_matrix(self):
        cases = (
            (None, False, False, False),
            (self.regular_user, False, False, False),
            (self.editor, False, True, False),
            (self.owner, True, True, True),
        )
        for user, can_create, can_update, can_delete in cases:
            with self.subTest(user=getattr(user, "username", "anonymous")):
                self.client.logout()
                if user is not None:
                    self.client.force_login(user)
                response = self.client.get(self.list_url)
                if can_create:
                    self.assertContains(response, f'href="{self.create_url}"')
                else:
                    self.assertNotContains(response, f'href="{self.create_url}"')
                self.assertContains(
                    response,
                    f'const CAN_UPDATE_EXPERIENCE = "{str(can_update).lower()}"',
                )
                self.assertContains(
                    response,
                    f'const CAN_DELETE_EXPERIENCE = "{str(can_delete).lower()}"',
                )

    def test_anonymous_star_redirects_to_login_without_changing_data(self):
        response = self.client.post(self.star_url)
        self.assertRedirects(
            response,
            f"{reverse('main:login')}?next={self.star_url}",
            fetch_redirect_response=False,
        )
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_star_rejects_get_and_missing_csrf(self):
        self.client.force_login(self.regular_user)
        self.assertEqual(self.client.get(self.star_url).status_code, 405)

        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.regular_user)
        self.assertEqual(csrf_client.post(self.star_url).status_code, 403)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_logged_in_user_can_star_and_unstar(self):
        self.client.force_login(self.regular_user)

        response = self.client.post(self.star_url)
        self.assertRedirects(response, self.list_url)
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.regular_user.pk).exists()
        )

        self.client.post(self.star_url)
        self.assertFalse(
            self.experience.starred_by.filter(pk=self.regular_user.pk).exists()
        )

    def test_stars_are_unique_and_independent_per_user(self):
        self.experience.starred_by.add(self.regular_user, self.other_user)
        self.experience.starred_by.add(self.regular_user)
        self.assertEqual(self.experience.starred_by.count(), 2)

        self.client.force_login(self.regular_user)
        self.client.post(self.star_url)
        self.assertFalse(
            self.experience.starred_by.filter(pk=self.regular_user.pk).exists()
        )
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.other_user.pk).exists()
        )

    def test_timeline_shows_star_status_and_total(self):
        self.experience.starred_by.add(self.regular_user, self.other_user)
        self.client.force_login(self.regular_user)
        response = self.client.get(self.json_url)
        fields = response.json()[0]["fields"]

        self.assertEqual(fields["star_count"], 2)
        self.assertTrue(fields["is_starred"])

    def test_anonymous_timeline_offers_login_without_post_form(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, "Log in to star")
        self.assertContains(response, 'const IS_AUTHENTICATED = "false"')

    def test_experience_json_does_not_expose_starring_users(self):
        self.experience.starred_by.add(self.regular_user)
        anonymous_response = self.client.get(self.json_url)
        fields = anonymous_response.json()[0]["fields"]
        self.assertNotIn("starred_by", fields)
        self.assertEqual(fields["star_count"], 1)
        self.assertFalse(fields["is_starred"])
        self.assertNotContains(anonymous_response, self.regular_user.username)

        self.client.force_login(self.regular_user)
        fields = self.client.get(self.json_url).json()[0]["fields"]
        self.assertTrue(fields["is_starred"])

    def test_unknown_star_target_returns_404_for_logged_in_user(self):
        self.client.force_login(self.regular_user)
        url = reverse("main:toggle_experience_star", args=[uuid.uuid4()])
        self.assertEqual(self.client.post(url).status_code, 404)

    def test_timeline_links_and_confirmation_identify_target(self):
        self.client.force_login(self.owner)
        response = self.client.get(self.list_url)
        self.assertContains(response, f'href="{self.create_url}"')
        self.assertContains(response, "EDIT_EXPERIENCE_URL_TEMPLATE")
        self.assertContains(response, "DELETE_EXPERIENCE_URL_TEMPLATE")
        self.assertContains(response, 'const CAN_UPDATE_EXPERIENCE = "true"')
        self.assertContains(response, 'const CAN_DELETE_EXPERIENCE = "true"')
        self.assertContains(response, "Keep experience")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_json_returns_manual_fields_and_model_ordering(self):
        earlier = Experience.objects.create(
            **{**self.data, "title": "Earlier Role", "display_order": 1}
        )
        response = self.client.get(self.json_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        payload = response.json()
        self.assertEqual([item["pk"] for item in payload],
                         [str(earlier.pk), str(self.experience.pk)])
        for field, value in self.data.items():
            self.assertEqual(payload[1]["fields"][field], value)
        fields = payload[1]["fields"]
        self.assertEqual(fields["category_display"], "Internship")
        self.assertEqual(fields["skill_list"], ["Advocacy", "Communication", "Teamwork"])
        self.assertEqual(fields["star_count"], 0)
        self.assertFalse(fields["is_starred"])
        self.assertTrue(fields["is_ongoing"])

    def test_json_search_matches_title_or_organization_case_insensitively(self):
        for query in ("  wElFaRe  ", "bEm"):
            with self.subTest(query=query):
                payload = self.client.get(self.json_url, {"q": query}).json()
                self.assertEqual([item["pk"] for item in payload], [str(self.experience.pk)])

    def test_json_combines_search_and_category(self):
        Experience.objects.create(
            **{**self.data, "title": "Another BEM Role", "category": "volunteer"}
        )
        payload = self.client.get(
            self.json_url, {"q": "BEM", "category": "internship"}
        ).json()
        self.assertEqual([item["pk"] for item in payload], [str(self.experience.pk)])

    def test_json_empty_and_unknown_filters_return_empty_arrays(self):
        for filters in ({"q": "No such role"}, {"category": "unknown"}):
            with self.subTest(filters=filters):
                response = self.client.get(self.json_url, filters)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), [])
        Experience.objects.all().delete()
        self.assertEqual(self.client.get(self.json_url).json(), [])

    def test_timeline_shell_preserves_filters_for_ajax_request(self):
        other = Experience.objects.create(
            **{**self.data, "title": "Excluded Role", "category": "research"}
        )
        response = self.client.get(
            self.list_url, {"q": " BEM ", "category": "internship"}
        )
        self.assertNotIn("experience_list", response.context)
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, other.title)
        self.assertContains(response, 'value="BEM"')
        self.assertContains(response, 'value="internship" selected')
        self.assertContains(response, "fetchExperiences")
        payload = self.client.get(
            self.json_url, {"q": " BEM ", "category": "internship"}
        ).json()
        self.assertEqual([item["pk"] for item in payload], [str(self.experience.pk)])
        self.assertContains(response, "Clear filters")

    def test_timeline_search_uses_debounce_and_immediate_category_filter(self):
        response = self.client.get(self.list_url)

        self.assertContains(response, "EXPERIENCE_SEARCH_DEBOUNCE_MS = 350")
        self.assertContains(
            response,
            'searchInput.addEventListener("input", scheduleExperienceFilters)',
        )
        self.assertContains(response, "window.clearTimeout(experiencesSearchTimeout)")
        self.assertContains(response, "window.setTimeout(() =>")
        self.assertContains(
            response,
            'categoryInput.addEventListener("change", () =>',
        )
        self.assertContains(response, "experiencesAbortController.abort()")

    def test_ajax_create_modal_and_script_are_only_available_to_owner(self):
        anonymous_response = self.client.get(self.list_url)
        self.assertNotContains(anonymous_response, 'id="add-experience-modal"')
        self.assertNotContains(anonymous_response, 'id="experience-form"')

        self.client.force_login(self.owner)
        owner_response = self.client.get(self.list_url)
        self.assertContains(
            owner_response,
            'popovertarget="add-experience-modal"',
        )
        self.assertContains(owner_response, 'id="add-experience-modal"')
        self.assertContains(owner_response, 'id="experience-form"')
        self.assertContains(owner_response, "CREATE_EXPERIENCE_ENDPOINT")
        self.assertContains(owner_response, 'getCookie("csrftoken")')
        self.assertContains(owner_response, "new FormData(experienceForm)")
        self.assertContains(owner_response, "displayExperienceFormErrors")
        self.assertContains(owner_response, "showToast(")
        self.assertContains(owner_response, "await fetchExperiences(")

    def test_filtered_empty_state_differs_from_empty_database(self):
        response = self.client.get(self.list_url, {"q": "Missing"})
        self.assertContains(response, "No experiences match these filters.")
        self.assertEqual(
            self.client.get(self.json_url, {"q": "Missing"}).json(), []
        )
        Experience.objects.all().delete()
        response = self.client.get(self.list_url)
        self.assertContains(response, "No experiences have been added yet.")
        self.assertEqual(self.client.get(self.json_url).json(), [])


class CertificationTest(TestCase):
    def setUp(self):
        Certification.objects.all().delete()
        user_model = get_user_model()
        self.owner = user_model.objects.create_superuser(
            username="portfolio_owner",
            email="owner@example.com",
            password="OwnerTutorial4Pass!",
        )
        self.regular_user = user_model.objects.create_user(
            username="regular_reader",
            password="ReaderTutorial4Pass!",
        )
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

    def test_certifications_page_renders_ajax_shell_without_model_data(self):
        response = self.client.get(reverse("main:show_certifications"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certifications.html")
        self.assertNotContains(response, self.certification.title)
        self.assertContains(response, 'id="certificate-loading"')
        self.assertContains(response, 'id="certificate-error"')
        self.assertContains(response, 'id="certificate-empty"')
        self.assertContains(response, 'id="certificate-track"')
        self.assertContains(response, reverse("main:get_certifications_json"))

    def test_empty_certifications_page(self):
        Certification.objects.all().delete()
        response = self.client.get(reverse("main:show_certifications"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No certifications have been added yet.")
        self.assertContains(response, "fetchCertifications")

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
        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification_detail.html")
        self.assertEqual(response.context["certification"], self.certification)
        self.assertContains(response, self.certification.title)
        self.assertContains(response, self.certification.issuer)
        self.assertContains(response, self.certification.description)
        self.assertNotContains(response, "Delete certification")

    def test_certifications_page_builds_detail_links_from_json_ids(self):
        response = self.client.get(reverse("main:show_certifications"))

        self.assertContains(response, "DETAIL_URL_TEMPLATE")
        self.assertContains(response, "detailUrlFor(item.pk)")

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
        self.client.force_login(self.owner)
        response = self.client.get(reverse("main:create_certification"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification_form.html")
        self.assertIsInstance(response.context["form"], CertificationForm)
        self.assertContains(response, 'name="csrfmiddlewaretoken"')

    def test_valid_certification_submission_creates_object(self):
        self.client.force_login(self.owner)
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
        self.client.force_login(self.owner)
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

    def test_certifications_page_preserves_initial_search_for_ajax(self):
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

        self.assertNotContains(response, self.certification.title)
        self.assertNotContains(response, other_certification.title)
        self.assertContains(response, 'value="Gemini"')
        self.assertContains(response, "SEARCH_DEBOUNCE_DELAY = 300")

    def test_certification_search_has_contextual_empty_state(self):
        response = self.client.get(
            reverse("main:show_certifications"),
            {"title": "Unknown credential"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No certifications match")
        self.assertContains(response, "Unknown credential")

    def test_certification_page_includes_debounce_xss_and_toast_protection(self):
        response = self.client.get(reverse("main:show_certifications"))

        self.assertContains(response, "function escapeHtml(value)")
        self.assertContains(response, "clearTimeout(searchDebounceTimer)")
        self.assertContains(response, "new AbortController()")
        self.assertContains(response, "showToast(")
        self.assertContains(response, 'id="toast-component"')

    def test_create_certification_ajax_rejects_get(self):
        self.client.force_login(self.owner)
        response = self.client.get(
            reverse("main:create_certification_ajax")
        )

        self.assertEqual(response.status_code, 405)

    def test_create_certification_ajax_returns_json_403_for_non_owner(self):
        endpoint = reverse("main:create_certification_ajax")

        anonymous_response = self.client.post(endpoint, {})
        self.assertEqual(anonymous_response.status_code, 403)
        self.assertEqual(
            anonymous_response["Content-Type"],
            "application/json",
        )

        self.client.force_login(self.regular_user)
        regular_response = self.client.post(endpoint, {})
        self.assertEqual(regular_response.status_code, 403)
        self.assertIn("message", regular_response.json())

    def test_create_certification_ajax_returns_validation_errors(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            reverse("main:create_certification_ajax"),
            {
                "title": "",
                "issuer": "Udemy",
                "category": "course",
                "issued_year": 2026,
                "image_path": "img/certificates/course.png",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])
        self.assertEqual(Certification.objects.count(), 1)

    def test_create_certification_ajax_creates_object_with_201(self):
        self.client.force_login(self.owner)
        response = self.client.post(
            reverse("main:create_certification_ajax"),
            {
                "title": "JavaScript Foundations",
                "issuer": "Open Learning",
                "category": "course",
                "issued_year": 2026,
                "image_path": "img/certificates/javascript.png",
                "credential_url": "https://example.com/javascript",
                "description": "Asynchronous JavaScript and the DOM.",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("pk", response.json())
        self.assertTrue(
            Certification.objects.filter(
                title="JavaScript Foundations"
            ).exists()
        )

    def test_create_certification_ajax_requires_csrf_token(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.owner)
        response = csrf_client.post(
            reverse("main:create_certification_ajax"),
            {
                "title": "Blocked request",
                "issuer": "Test issuer",
                "category": "course",
                "issued_year": 2026,
                "image_path": "img/certificates/blocked.png",
            },
        )

        self.assertEqual(response.status_code, 403)
        self.assertFalse(
            Certification.objects.filter(title="Blocked request").exists()
        )

    def test_certification_form_strips_html_from_text_fields(self):
        form = CertificationForm(
            data={
                "title": "<b>Safe title</b>",
                "issuer": "<i>Safe issuer</i>",
                "category": "course",
                "issued_year": 2026,
                "image_path": "<span>img/certificates/safe.png</span>",
                "credential_url": "",
                "description": "Learned <strong>safe rendering</strong>.",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        certification = form.save()
        self.assertEqual(certification.title, "Safe title")
        self.assertEqual(certification.issuer, "Safe issuer")
        self.assertEqual(
            certification.image_path,
            "img/certificates/safe.png",
        )
        self.assertEqual(
            certification.description,
            "Learned safe rendering.",
        )

    def test_certification_form_rejects_title_containing_only_xss_tag(self):
        form = CertificationForm(
            data={
                "title": '<img src="x" onerror="alert(\'XSS!\')">',
                "issuer": "Test issuer",
                "category": "course",
                "issued_year": 2026,
                "image_path": "img/certificates/xss.png",
                "credential_url": "",
                "description": "Security test",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_delete_certification_rejects_get_requests(self):
        self.client.force_login(self.owner)
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
        csrf_client.force_login(self.owner)
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
        self.client.force_login(self.owner)
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
        self.client.force_login(self.owner)
        response = self.client.post(
            reverse(
                "main:delete_certification",
                kwargs={"certification_id": uuid.uuid4()},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_anonymous_star_redirects_to_login_without_changing_data(self):
        star_url = reverse(
            "main:toggle_certification_star", args=[self.certification.pk]
        )
        response = self.client.post(star_url)
        self.assertRedirects(
            response,
            f'{reverse("main:login")}?next={star_url}',
        )
        self.assertEqual(self.certification.starred_by.count(), 0)

    def test_authenticated_star_endpoint_is_post_only(self):
        self.client.force_login(self.regular_user)
        response = self.client.get(
            reverse("main:toggle_certification_star", args=[self.certification.pk])
        )
        self.assertEqual(response.status_code, 405)
        self.assertEqual(self.certification.starred_by.count(), 0)

    def test_certification_star_requires_csrf_token(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.regular_user)
        response = client.post(
            reverse("main:toggle_certification_star", args=[self.certification.pk])
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.certification.starred_by.count(), 0)

    def test_regular_user_can_toggle_one_star(self):
        self.client.force_login(self.regular_user)
        star_url = reverse(
            "main:toggle_certification_star", args=[self.certification.pk]
        )
        detail_url = reverse(
            "main:show_certification_detail", args=[self.certification.pk]
        )

        response = self.client.post(star_url)
        self.assertRedirects(response, detail_url)
        self.assertEqual(self.certification.starred_by.count(), 1)
        self.assertTrue(self.certification.starred_by.filter(pk=self.regular_user.pk).exists())

        response = self.client.post(star_url)
        self.assertRedirects(response, detail_url)
        self.assertEqual(self.certification.starred_by.count(), 0)

    def test_multiple_users_have_independent_stars(self):
        self.certification.starred_by.add(self.regular_user, self.owner)
        self.certification.starred_by.add(self.regular_user)
        self.assertEqual(self.certification.starred_by.count(), 2)
        self.assertQuerySetEqual(
            self.regular_user.starred_certifications.all(),
            [self.certification],
        )

    def test_star_component_displays_count_and_current_user_state(self):
        detail_url = reverse(
            "main:show_certification_detail", args=[self.certification.pk]
        )
        anonymous_response = self.client.get(detail_url)
        self.assertContains(anonymous_response, "Star")
        self.assertNotContains(anonymous_response, "Unstar")
        self.assertContains(anonymous_response, 'aria-label="0 stars"')

        self.certification.starred_by.add(self.regular_user)
        self.client.force_login(self.regular_user)
        authenticated_response = self.client.get(detail_url)
        self.assertContains(authenticated_response, "Unstar")
        self.assertContains(authenticated_response, "is-starred")
        self.assertContains(authenticated_response, 'aria-label="1 stars"')

    def test_certification_json_exposes_star_state_without_user_identities(self):
        self.certification.starred_by.add(self.regular_user, self.owner)
        anonymous_fields = self.client.get(
            reverse("main:get_certifications_json")
        ).json()[0]["fields"]
        self.assertEqual(anonymous_fields["star_count"], 2)
        self.assertFalse(anonymous_fields["is_starred"])
        self.assertNotIn("starred_by", anonymous_fields)
        self.assertNotContains(
            self.client.get(reverse("main:get_certifications_json")),
            self.regular_user.username,
        )

        self.client.force_login(self.regular_user)
        authenticated_fields = self.client.get(
            reverse("main:get_certifications_json")
        ).json()[0]["fields"]
        self.assertTrue(authenticated_fields["is_starred"])

    def test_unknown_certification_star_returns_404_for_logged_in_user(self):
        self.client.force_login(self.regular_user)
        response = self.client.post(
            reverse("main:toggle_certification_star", args=[uuid.uuid4()])
        )
        self.assertEqual(response.status_code, 404)

    def test_anonymous_users_are_redirected_before_mutating_certifications(self):
        create_response = self.client.get(reverse("main:create_certification"))
        delete_response = self.client.post(
            reverse("main:delete_certification", args=[self.certification.pk])
        )
        self.assertRedirects(
            create_response,
            f'{reverse("main:login")}?next={reverse("main:create_certification")}',
        )
        self.assertRedirects(
            delete_response,
            f'{reverse("main:login")}?next='
            f'{reverse("main:delete_certification", args=[self.certification.pk])}',
        )
        self.assertTrue(Certification.objects.filter(pk=self.certification.pk).exists())

    def test_regular_users_receive_403_for_create_and_delete(self):
        self.client.force_login(self.regular_user)
        self.assertEqual(
            self.client.get(reverse("main:create_certification")).status_code,
            403,
        )
        self.assertEqual(
            self.client.post(
                reverse("main:delete_certification", args=[self.certification.pk])
            ).status_code,
            403,
        )
        self.assertTrue(Certification.objects.filter(pk=self.certification.pk).exists())

    def test_mutation_controls_follow_superuser_permissions(self):
        list_url = reverse("main:show_certifications")
        detail_url = reverse("main:show_certification_detail", args=[self.certification.pk])
        delete_url = reverse("main:delete_certification", args=[self.certification.pk])

        for user in (None, self.regular_user):
            with self.subTest(user=user):
                self.client.logout()
                if user:
                    self.client.force_login(user)
                self.assertNotContains(
                    self.client.get(list_url),
                    'popovertarget="add-certification-modal"',
                )
                self.assertNotContains(self.client.get(detail_url), f'action="{delete_url}"')

        self.client.force_login(self.owner)
        owner_list = self.client.get(list_url)
        self.assertContains(
            owner_list,
            'popovertarget="add-certification-modal"',
        )
        self.assertContains(owner_list, 'id="certification-form"')
        self.assertContains(owner_list, 'name="csrfmiddlewaretoken"')
        owner_detail = self.client.get(detail_url)
        self.assertContains(owner_detail, f'action="{delete_url}"')
        self.assertContains(owner_detail, 'name="csrfmiddlewaretoken"')
