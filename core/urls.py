from django.urls import path

from core import views

urlpatterns = [
    # home
    path("", views.index, name="index"),
    # sign up page
    path("signup/", views.SignUpView.as_view(), name="signup"),
    # pack
    path("pack/new/", views.PackCreateView.as_view(), name="pack_create"),
    path("packs/", views.PackListView.as_view(), name="packs_list"),
    path("pack/<int:pk>/", views.PackUpdateView.as_view(), name="pack_update"),
    path("pack/<int:pk>/delete/", views.PackDeleteView.as_view(), name="pack_delete"),
    # bag
    path("bag/new/", views.BagCreateView.as_view(), name="bag_create"),
    path("bags/", views.BagListView.as_view(), name="bags_list"),
    path("bag/<int:pk>/", views.BagUpdateView.as_view(), name="bag_update"),
    path("bag/<int:pk>/delete/", views.BagDeleteView.as_view(), name="bag_delete"),
    # item
    path("item/new/", views.ItemCreateView.as_view(), name="item_create"),
    path("items/", views.ItemListView.as_view(), name="items_list"),
    path("item/<int:pk>/", views.ItemUpdateView.as_view(), name="item_update"),
    path("item/<int:pk>/delete/", views.ItemDeleteView.as_view(), name="item_delete"),
]
