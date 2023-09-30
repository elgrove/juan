import logging
from core.forms import BagForm, ItemForm, PackForm
from core.models import Bag, Item, Pack
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "core/index.html", {})


class PackCreateView(CreateView):
    model = Pack
    form_class = PackForm
    template_name = "core/pack.html"

    def get_success_url(self):
        return reverse_lazy("packs_list")


class PackUpdateView(UpdateView):
    model = Pack
    form_class = PackForm
    template_name = "core/pack.html"

    def get_success_url(self):
        return reverse_lazy("packs_list")


class PackListView(ListView):
    model = Pack
    template_name = "core/packs.html"
    context_object_name = "packs"
    ordering = ["-modified_at"]


class BagCreateView(CreateView):
    model = Bag
    form_class = BagForm
    template_name = "core/bag.html"

    def get_success_url(self):
        return reverse_lazy("bags_list")


class BagUpdateView(UpdateView):
    model = Bag
    form_class = BagForm
    template_name = "core/bag.html"

    def get_success_url(self):
        return reverse_lazy("bags_list")


class BagListView(ListView):
    model = Bag
    template_name = "core/bags.html"
    context_object_name = "bags"
    ordering = ["-modified_at"]


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "core/item.html"

    def get_success_url(self):
        return reverse_lazy("items_list")


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "core/item.html"

    def get_success_url(self):
        return reverse_lazy("items_list")


class ItemListView(ListView):
    model = Item
    template_name = "core/items.html"
    context_object_name = "items"
    ordering = ["-modified_at"]

    @property
    def categories(self):
        return list({item.category for item in self.object_list})

    @property
    def category_map(self):
        return {
            category: [item for item in self.object_list if item.category == category]
            for category in self.categories
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_map"] = self.category_map
        return context
