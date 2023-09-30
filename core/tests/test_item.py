from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse

from core.forms import ItemForm
from core.models import Item

TEST_ITEM = {
    "name": "TestItem",
    "description": "Test Description",
    "category": "Test Category",
}


class ItemFormTest(TestCase):
    def test_valid_form(self):
        data = TEST_ITEM
        form = ItemForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {}
        form = ItemForm(data)
        self.assertFalse(form.is_valid())


class ItemCreateViewTest(TestCase):
    def test_view_url(self):
        response = self.client.get(reverse("item_create"))
        self.assertEqual(response.status_code, 200)

    def test_create_success(self):
        data = TEST_ITEM
        response = self.client.post(reverse("item_create"), data)
        assert response.status_code == 302

        query_item = Item.objects.first()
        assert query_item.name == "TestItem"


class ItemUpdateViewTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(**TEST_ITEM)

    def test_view_url(self):
        response = self.client.get(reverse("item_update", args=[str(self.item.id)]))
        self.assertEqual(response.status_code, 200)

    def test_update_success(self):
        item = Item.objects.first()
        item.name = "RenamedItem"
        response = self.client.post(
            reverse("item_update", args=[str(self.item.id)]),
            model_to_dict(item),
        )
        assert response.status_code == 302

        query_item = Item.objects.first()
        assert query_item.name == "RenamedItem"


class ItemListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_items = 50
        for item_id in range(number_of_items):
            Item.objects.create(name=f"Item {item_id}", category="Electronics")

    def test_view_url_exists(self):
        response = self.client.get("/items/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("items_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/items.html")

    def test_context_category_map(self):
        response = self.client.get(reverse("items_list"))
        self.assertTrue("category_map" in response.context)
        self.assertIn("Electronics", response.context["category_map"])
