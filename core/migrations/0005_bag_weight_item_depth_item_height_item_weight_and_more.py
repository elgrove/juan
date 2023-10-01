# Generated by Django 4.2.5 on 2023-10-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_pack_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="bag",
            name="weight",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="depth",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="height",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="weight",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="width",
            field=models.PositiveIntegerField(null=True),
        ),
    ]