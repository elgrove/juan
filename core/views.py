from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from core.forms import BagForm, ItemForm, PackForm

from core.models import Bag, Item, Pack


# index select packs, items or bags
# pack view
# bag view
# items view


def index(request):
    packs = Pack.objects.all().order_by("-modified_at")
    context = {"packs": packs}
    return render(request, "core/index.html", context)


def pack_view(request, pack_id=None):
    if pack_id:
        pack = get_object_or_404(Pack, pk=pack_id)
        form = PackForm(instance=pack)
    else:
        form = PackForm()

    if request.method == "POST":
        if pack_id:
            form = PackForm(request.POST, instance=pack)
        else:
            form = PackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)

    context = {"form": form, "pack_id": pack_id}
    return render(request, "core/pack.html", context)


def bag_view(request, bag_id=None):
    if bag_id:
        bag = get_object_or_404(Bag, pk=bag_id)
        form = BagForm(instance=bag)
    else:
        form = BagForm()

    if request.method == "POST":
        if bag_id:
            form = BagForm(request.POST, instance=bag)
        else:
            form = BagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)

    context = {"form": form, "bag_id": bag_id}
    return render(request, "core/bag.html", context)


def item_view(request, item_id=None):
    if item_id:
        item = get_object_or_404(Item, pk=item_id)
        form = ItemForm(instance=item)
    else:
        form = ItemForm()

    if request.method == "POST":
        if item_id:
            form = ItemForm(request.POST, instance=item)
        else:
            form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)  # Redirects to the same URL

    context = {"form": form, "item_id": item_id}
    return render(request, "core/item.html", context)
