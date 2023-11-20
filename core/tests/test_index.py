from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_view_url_exists(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "core/index.html")
