# Generated by Django 4.2.5 on 2023-10-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_bag_weight_item_depth_item_height_item_weight_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bag",
            name="depth",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="bag",
            name="height",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="bag",
            name="width",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
