from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Bag(Base):
    pass


class Pack(Base):
    bag = models.OneToOneField(Bag, on_delete=models.CASCADE)
    items = models.ManyToManyField("Item", related_name="packs")


class Item(Base):
    category = models.CharField(max_length=32)
