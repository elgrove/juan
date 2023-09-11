from core.forms import BagForm, ItemForm, PackForm
from core.models import Bag, Item, Pack
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

# index select packs, items or bags
# pack view
# bag view
# items view


def index(request):
    return render(request, "core/index.html", {})


class PackCreateView(CreateView):
    model = Pack
    form_class = PackForm
    template_name = "core/pack.html"

    def get_success_url(self):
        return reverse_lazy("packs_list")


class BagCreateView(CreateView):
    model = Bag
    form_class = BagForm
    template_name = "core/bag.html"

    def get_success_url(self):
        return reverse_lazy("bags_list")


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "core/item.html"

    def get_success_url(self):
        return reverse_lazy("items_list")


class PackUpdateView(UpdateView):
    model = Pack
    form_class = PackForm
    template_name = "core/pack.html"

    def get_success_url(self):
        return reverse_lazy("packs_list")


class BagUpdateView(UpdateView):
    model = Bag
    form_class = BagForm
    template_name = "core/bag.html"

    def get_success_url(self):
        return reverse_lazy("bags_list")


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


class BagListView(ListView):
    model = Bag
    template_name = "core/bags.html"
    context_object_name = "bags"
    ordering = ["-modified_at"]


class PackListView(ListView):
    model = Pack
    template_name = "core/packs.html"
    context_object_name = "packs"
    ordering = ["-modified_at"]
