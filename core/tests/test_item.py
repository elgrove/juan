from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse

from core.forms import ItemForm
from core.models import Item, Pack
from core.tests import TEST_DIMENSIONS, UserLoggedInTestCase

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


class ItemCreateViewTest(UserLoggedInTestCase):
    def test_view_url(self):
        response = self.client.get(reverse("item_create"))
        self.assertEqual(response.status_code, 200)

    def test_create_success(self):
        data = TEST_ITEM
        response = self.client.post(reverse("item_create"), data)
        assert response.status_code == 302

        query_item = Item.objects.first()
        assert query_item.name == "TestItem"


class ItemUpdateViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
            **TEST_ITEM, **TEST_DIMENSIONS, user_id=self.user.id
        )

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


class ItemListViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        number_of_items = 50
        for item_id in range(number_of_items):
            Item.objects.create(
                name=f"Item {item_id}", category="Electronics", user_id=self.user.id
            )

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


class ItemDeleteViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
            **TEST_ITEM, **TEST_DIMENSIONS, user_id=self.user.id
        )
        self.related_pack = Pack.objects.create(name="TestPack", user_id=self.user.id)
        self.related_pack.items.set([self.item])

    def test_view_url(self):
        response = self.client.get(
            reverse("item_delete", kwargs={"pk": str(self.item.pk)})
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_confirm_page_related_packs(self):
        response = self.client.get(
            reverse("item_delete", kwargs={"pk": str(self.item.pk)})
        )
        self.assertContains(response, "TestPack")

    def test_delete_detaches_from_related_pack(self):
        _ = self.client.post(reverse("item_delete", kwargs={"pk": str(self.item.pk)}))
        related_pack = Pack.objects.get(id=self.related_pack.pk)
        items = related_pack.items.get_queryset().all()
        self.assertNotIn(self.item, items)

    def test_delete_success(self):
        response = self.client.post(
            reverse("item_delete", kwargs={"pk": str(self.item.pk)})
        )
        self.assertEquals(response.status_code, 302)
