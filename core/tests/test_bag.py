from django.test import TestCase
from django.urls import reverse
from core.models import Bag
from core.forms import BagForm
from django.forms.models import model_to_dict


class BagFormTest(TestCase):
    def test_valid_form(self):
        data = {"name": "TestBag", "description": "Test Description"}
        form = BagForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {}
        form = BagForm(data)
        self.assertFalse(form.is_valid())


class BagCreateViewTest(TestCase):
    def test_view_url(self):
        response = self.client.get(reverse("bag_create"))
        self.assertEqual(response.status_code, 200)

    def test_create_success(self):
        data = {"name": "TestBag"}
        response = self.client.post(reverse("bag_create"), data)
        assert response.status_code == 302

        query_bag = Bag.objects.first()
        assert query_bag.name == "TestBag"


class BagUpdateViewTest(TestCase):
    def setUp(self):
        self.bag = Bag.objects.create(name="TestBag", description="test description")

    def test_view_url(self):
        response = self.client.get(reverse("bag_update", args=[str(self.bag.id)]))
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
