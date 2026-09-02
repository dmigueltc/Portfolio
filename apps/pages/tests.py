from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class FoundationCheckTests(TestCase):
    def test_foundation_page_responds(self):
        response = self.client.get(reverse("pages:foundation-check"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/foundation-check.html")
        self.assertContains(response, "Development Foundation V1")

    def test_admin_is_available(self):
        response = self.client.get("/admin/login/")

        self.assertEqual(response.status_code, 200)

    def test_foundation_page_uses_static_asset(self):
        response = self.client.get(reverse("pages:foundation-check"))

        self.assertContains(response, "/static/css/base.css")

    def test_foundation_languages_are_configured(self):
        self.assertEqual(settings.LANGUAGE_CODE, "pt-pt")
        self.assertEqual(
            {code for code, _ in settings.LANGUAGES},
            {"pt-pt", "en", "fr"},
        )
