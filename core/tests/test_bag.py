from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse

from core.forms import BagForm
from core.models import Bag, Pack
from django.contrib.auth.models import User

from core.tests import TEST_DIMENSIONS, UserLoggedInTestCase

TEST_BAG = {"name": "TestBag", "description": "Test Description"}


class BagFormTest(TestCase):
    def test_valid_form(self):
        form = BagForm(TEST_BAG)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {}
        form = BagForm(data)
        self.assertFalse(form.is_valid())


class BagCreateViewTest(UserLoggedInTestCase):
    def test_view_url(self):
        response = self.client.get(reverse("bag_create"))
        self.assertEqual(response.status_code, 200)

    def test_create_success(self):
        data = {"name": "TestBag"}
        response = self.client.post(reverse("bag_create"), data)
        assert response.status_code == 302

        query_bag = Bag.objects.first()
        assert query_bag.name == "TestBag"


class BagUpdateViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.bag = Bag.objects.create(
            name="TestBag",
            description="test description",
            user_id=self.user.id,
            **TEST_DIMENSIONS,
        )

    def test_view_url(self):
        response = self.client.get(
            reverse("bag_update", kwargs={"pk": str(self.bag.pk)})
        )
        self.assertEqual(response.status_code, 200)

    def test_update_success(self):
        bag = Bag.objects.first()
        bag.name = "RenamedBag"
        response = self.client.post(
            reverse("bag_update", args=[str(self.bag.id)]),
            model_to_dict(bag),
        )
        assert response.status_code == 302

        query_bag = Bag.objects.first()
        assert query_bag.name == "RenamedBag"


class BagDeleteViewTest(UserLoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.bag = Bag.objects.create(
            name="TestBag",
            description="test description",
            user_id=self.user.id,
            weight=1,
            height=1,
            width=1,
            depth=1,
        )
        self.related_pack = Pack.objects.create(
            name="TestPack", bag=self.bag, user_id=self.user.id
        )

    def test_view_url(self):
        response = self.client.get(
            reverse("bag_delete", kwargs={"pk": str(self.bag.pk)})
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_confirm_page_related_packs(self):
        response = self.client.get(
            reverse("bag_delete", kwargs={"pk": str(self.bag.pk)})
        )
        self.assertContains(response, "TestPack")

    def test_delete_detaches_from_related_pack(self):
        _ = self.client.post(reverse("bag_delete", kwargs={"pk": str(self.bag.pk)}))
        related_pack = Pack.objects.get(id=self.related_pack.pk)
        self.assertEqual(related_pack.bag, None)

    def test_delete_success(self):
        response = self.client.get(
            reverse("bag_delete", kwargs={"pk": str(self.bag.pk)})
        )
        self.assertEquals(response.status_code, 200)
        response = self.client.post(
            reverse("bag_delete", kwargs={"pk": str(self.bag.pk)})
        )
        self.assertEquals(response.status_code, 302)
