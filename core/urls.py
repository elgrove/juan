from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pack/<int:pack_id>/", views.pack_view, name="pack_view"),
    path("bag/<int:bag_id>/", views.bag_view, name="bag_view"),
    path("item/<int:item_id>/", views.item_view, name="item_view"),
    path("items/", views.items_view, name="items_view"),
    path("packs/", views.packs_view, name="packs_view"),
    path("bags/", views.bags_view, name="bags_view"),
]
