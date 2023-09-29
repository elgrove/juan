import logging
from django import forms

from . import models

logger = logging.getLogger(__name__)


class BagForm(forms.ModelForm):
    class Meta:
        model = models.Bag
        fields = ["name", "description"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ["name", "description", "category"]


class PackForm(forms.ModelForm):
    class Meta:
        model = models.Pack
        fields = ["name", "description", "bag", "items"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["bag"].queryset = models.Bag.objects.all()
        self.fields["items"].queryset = models.Item.objects.all()

        if not self.instance.pk:
            self.selected_items = []
        else:
            self.selected_items = list(self.instance.items.values_list("id", flat=True))

        self.category_choices = {}
        for item in models.Item.objects.all():
            self.category_choices.setdefault(item.category, []).append(
                (item.id, item.name)
            )
