from django.urls import reverse

from core.forms import PackForm
from core.models import Bag, Item, Pack
from core.tests import UserLoggedInTestCase

TEST_PACK = {"name": "TestPack", "description": "Test Description"}


class PackCreateViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.bag = Bag.objects.create(name="TestBag", user_id=self.user.id)
        self.item = Item.objects.create(
            name="TestItem", category="TestCategory", user_id=self.user.id
        )
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


class PackDeleteViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.pack = Pack.objects.create(
            name="TestPack", description="test description", user_id=self.user.id
        )
        self.related_item = Item.objects.create(name="TestItem", user_id=self.user.id)
        self.pack.items.set([self.related_item])
        self.related_bag = Bag.objects.create(name="TestBag", user_id=self.user.id)
        self.pack.bag = self.related_bag

    def test_view_url(self):
        response = self.client.get(
            reverse("pack_delete", kwargs={"pk": str(self.pack.pk)})
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_confirm_page_related_items_and_bag(self):
        response = self.client.get(
            reverse("pack_delete", kwargs={"pk": str(self.pack.pk)})
        )
        self.assertContains(response, "TestPack")

    def test_delete_does_not_delete_related_items_and_bag(self):
        _ = self.client.post(reverse("pack_delete", kwargs={"pk": str(self.pack.pk)}))
        items = Item.objects.all()
        bags = Bag.objects.all()
        self.assertTrue(items.exists())
        self.assertTrue(bags.exists())

    def test_delete_success(self):
        response = self.client.post(
            reverse("pack_delete", kwargs={"pk": str(self.pack.pk)})
        )
        self.assertEquals(response.status_code, 302)
