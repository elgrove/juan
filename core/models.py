from django.db import models


class Base(models.Model):
    """Abstract base model with some descriptive fields."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta indicating abstract class."""

        abstract = True

    def __str__(self):
        """Str returns object.name."""
        return str(self.name)


class Item(Base):
    """Object presenting an Item in a Pack.

    A Pack can have many items.

    An Item can be used by many Packs.
    """

    category = models.CharField(max_length=32)


class Bag(Base):
    """Object presenting a Bag of a Pack.

    A Bag can be used by many packs.
    """


class Pack(Base):
    """Object representing a Pack, with a bag and items.

    A Pack can have only one bag.

    A Pack can have many items.
    """

    bag = models.ForeignKey(
        Bag, on_delete=models.SET_NULL, null=True, related_name="packs"
    )
    items = models.ManyToManyField("Item", blank=True, related_name="packs")
