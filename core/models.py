from django.contrib.auth.models import User
from django.db import models


class Base(models.Model):
    """Abstract base model with some descriptive fields."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta indicating abstract class."""

        abstract = True

    def __str__(self):
        """Str returns object.name."""
        return str(self.name)


class DimensionsMixin(models.Model):
    """Mixin class used to add dimension fields to other models."""

    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    depth = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        """Meta indicating abstract class."""

        abstract = True

    @property
    def dimensions(self):
        """Returns a tuple with the dimensions of the object."""
        return (self.height, self.width, self.depth)

    @property
    def weight_kilos(self):
        """Returns the item's weight in kilos."""
        return self.weight / 1000


class Item(DimensionsMixin, Base):
    """Object presenting an Item in a Pack.

    A Pack can have many items.

    An Item can be used by many Packs.
    """

    category = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bag(DimensionsMixin, Base):
    """Object presenting a Bag of a Pack.

    A Bag can be used by many packs.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Pack(Base):
    """Object representing a Pack, with a bag and items.

    A Pack can have only one bag. A Pack can have many items.

    A Pack can have one user, a User can have many packs.
    """

    bag = models.ForeignKey(
        Bag, on_delete=models.SET_NULL, null=True, related_name="packs"
    )
    items = models.ManyToManyField("Item", blank=True, related_name="packs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
