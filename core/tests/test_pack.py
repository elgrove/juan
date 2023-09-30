from django.test import TestCase
from django.urls import reverse

from core.forms import PackForm
from core.models import Bag, Item


class PackCreateViewTest(TestCase):
    def setUp(self):
        self.bag = Bag.objects.create(name="TestBag")
        self.item = Item.objects.create(name="TestItem", category="TestCategory")
        self.create_url = reverse("pack_create")

    def test_view_uses_correct_form(self):
        response = self.client.get(self.create_url)
        self.assertIsInstance(response.context["form"], PackForm)

    def test_pack_create_success(self):
        data = {
            "name": "TestPack",
            "description": "test description",
            "bag": self.bag.id,
            "items": [self.item.id],
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("packs_list"))
