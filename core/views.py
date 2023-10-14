import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from core.forms import BagForm, ItemForm, PackForm
from core.models import Bag, Item, Pack

logger = logging.getLogger(__name__)


def index(request):
    """View returning the home page."""
    return render(request, "core/index.html", {})


class PackCreateView(CreateView):
    """View for creating a Pack."""

    model = Pack
    form_class = PackForm
    template_name = "core/pack.html"

    def get_success_url(self):
        """Returns create success url."""
        return reverse_lazy("packs_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BagDeleteView(DeleteView):
    model = Bag
    success_url = reverse_lazy("bags_list")

    @property
    def related_packs(self):
        return self.object.packs.get_queryset().all()

    def get_context_data(self, **kwargs):
        """Extends generic view context."""
        context = super().get_context_data(**kwargs)
        context["related_packs"] = self.related_packs
        return context


class PackUpdateView(UpdateView):
    """View for updating a Pack."""

    model = Pack
    form_class = PackForm
    template_name = "core/pack.html"

    def get_success_url(self):
        """Returns update success url."""
        return reverse_lazy("packs_list")


class PackListView(ListView):
    """View for listing Packs."""

    model = Pack
    template_name = "core/packs.html"
    context_object_name = "packs"
    ordering = ["-modified_at"]

    def get_queryset(self):
        return Pack.objects.filter(user=self.request.user).order_by(self.ordering[0])


class PackDeleteView(DeleteView):
    model = Pack
    success_url = reverse_lazy("packs_list")


class BagCreateView(CreateView):
    """View for creating a Bag."""

    model = Bag
    form_class = BagForm
    template_name = "core/bag.html"

    def get_success_url(self):
        """Returns create success url."""
        return reverse_lazy("bags_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BagUpdateView(UpdateView):
    """View for updating a Bag."""

    model = Bag
    form_class = BagForm
    template_name = "core/bag.html"

    def get_success_url(self):
        """Returns update success url."""
        return reverse_lazy("bags_list")


class BagListView(ListView):
    """View for listing Bags."""

    model = Bag
    template_name = "core/bags.html"
    context_object_name = "bags"
    ordering = ["-modified_at"]

    def get_queryset(self):
        return Bag.objects.filter(user=self.request.user).order_by(self.ordering[0])


class ItemCreateView(CreateView):
    """View to create an Item."""

    model = Item
    form_class = ItemForm
    template_name = "core/item.html"

    def get_success_url(self):
        """Returns create success url."""
        return reverse_lazy("items_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    """View to update an Item."""

    model = Item
    form_class = ItemForm
    template_name = "core/item.html"

    def get_success_url(self):
        """Returns update success url."""
        return reverse_lazy("items_list")


class ItemListView(ListView):
    """View for listing Items."""

    model = Item
    template_name = "core/items.html"
    context_object_name = "items"
    ordering = ["-modified_at"]

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user).order_by(self.ordering[0])

    @property
    def categories(self):
        """Returns list of unique item categories present on all items."""
        return list({item.category for item in self.object_list})

    @property
    def category_map(self):
        """Returns dict of shape {<item category>: [<items of that category>], ... }"""
        return {
            category: [item for item in self.object_list if item.category == category]
            for category in self.categories
        }

    def get_context_data(self, **kwargs):
        """Extends generic view context."""
        context = super().get_context_data(**kwargs)
        context["category_map"] = self.category_map
        return context


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy("items_list")

    @property
    def related_packs(self):
        return self.object.packs.get_queryset().all()

    def get_context_data(self, **kwargs):
        """Extends generic view context."""
        context = super().get_context_data(**kwargs)
        context["related_packs"] = self.related_packs
        return context
