from django import forms
from . import models


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
        print(self.fields["bag"].queryset)  # Debugging line
        print(self.fields["items"].queryset)  # Debugging line
