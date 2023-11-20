import logging

from django import forms

from core.models import Bag, Item, Pack

logger = logging.getLogger(__name__)


class BagForm(forms.ModelForm):
    """Form for creating/updating a Bag."""

    class Meta:
        """Meta."""

        model = Bag
        fields = ["name", "description", "weight", "height", "width", "depth"]

    def __init__(self, *args, **kwargs):
        """Override inherited init to mark required fields with asterisk."""
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.label = f"{field.label}*"


class ItemForm(forms.ModelForm):
    """Form for creating/updating an Item."""

    class Meta:
        """Meta."""

        model = Item
        fields = [
            "name",
            "category",
            "description",
            "weight",
            "height",
            "width",
            "depth",
        ]

    def __init__(self, *args, **kwargs):
        """Override inherited init to mark required fields with asterisk."""
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.label = f"{field.label}*"


class PackForm(forms.ModelForm):
    """Form for creating/updating an Pack."""

    class Meta:
        """Meta."""

        model = Pack
        fields = ["name", "description", "bag", "items"]

    def __init__(self, *args, **kwargs):
        """Initialise with logic to pre-select a pack's item checkboxes."""
        super().__init__(*args, **kwargs)
        self.fields["bag"].queryset = Bag.objects.all()
        self.fields["items"].queryset = Item.objects.all()
        self.selected_items = []
        self.category_choices = {}

        # if not self.instance.pk:
        #     return

        # self.selected_items = list(self.instance.items.values_list("id", flat=True))

        # for item in Item.objects.all():
        #     self.category_choices.setdefault(item.category, []).append(
        #         (item.id, item.name)
        #     )

        if not self.instance.pk:
            self.selected_items = []
        else:
            self.selected_items = list(self.instance.items.values_list("id", flat=True))

        self.category_choices = {}
        for item in Item.objects.all():
            self.category_choices.setdefault(item.category, []).append(
                (item.id, item.name)
            )
