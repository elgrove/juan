from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from core.models import Bag, Item, Pack


# index select packs, items or bags
# pack view
# bag view
# items view


def index(request):
    packs = Pack.objects.all().order_by("-modified_at")
    context = {"packs": packs}
    return render(request, "core/index.html", context)


def pack_view(request, pack_id):
    pack = get_object_or_404(Pack, pk=pack_id)
    context = {"pack": pack}
    return render(request, "core/pack.html", context)


def bag_view(request, bag_id):
    bag = get_object_or_404(Bag, pk=bag_id)
    context = {"bag": bag}
    return render(request, "core/bag.html", context)


def item_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {"item": item}
    return render(request, "core/item.html", context)
