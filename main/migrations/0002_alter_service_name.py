# Generated by Django 4.1.4 on 2023-12-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(max_length=250),
        ),
    ]
