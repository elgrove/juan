from django.contrib import admin

from .models import Bag, Item, Pack

admin.site.register(Pack)
admin.site.register(Bag)
admin.site.register(Item)
