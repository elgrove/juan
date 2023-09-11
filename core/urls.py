from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pack/<int:pk>/", views.PackUpdateView.as_view(), name="pack_update"),
    path("pack/", views.PackCreateView.as_view(), name="pack_create"),
    path("packs/", views.PackListView.as_view(), name="packs_list"),
    path("bag/<int:pk>/", views.BagUpdateView.as_view(), name="bag_update"),
    path("bag/", views.BagCreateView.as_view(), name="bag_create"),
    path("bags/", views.BagListView.as_view(), name="bags_list"),
    path("item/<int:pk>/", views.ItemUpdateView.as_view(), name="item_update"),
    path("item/", views.ItemCreateView.as_view(), name="item_create"),
    path("items/", views.ItemListView.as_view(), name="items_list"),
]
