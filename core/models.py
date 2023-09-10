from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Bag(Base):
    pass


class Pack(Base):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, related_name="packs")
    items = models.ManyToManyField("Item", related_name="packs")


class Item(Base):
    category = models.CharField(max_length=32)
