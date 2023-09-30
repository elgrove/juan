import logging
from django import forms

from core.models import Bag, Item, Pack

logger = logging.getLogger(__name__)


class BagForm(forms.ModelForm):
    class Meta:
        model = Bag
        fields = ["name", "description"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "category"]


class PackForm(forms.ModelForm):
    class Meta:
        model = Pack
        fields = ["name", "description", "bag", "items"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["bag"].queryset = Bag.objects.all()
        self.fields["items"].queryset = Item.objects.all()
        self.selected_items = []
        self.category_choices = {}

        if not self.instance.pk:
            return
        else:
            self.selected_items = list(self.instance.items.values_list("id", flat=True))

            for item in Item.objects.all():
                self.category_choices.setdefault(item.category, []).append(
                    (item.id, item.name)
                )
