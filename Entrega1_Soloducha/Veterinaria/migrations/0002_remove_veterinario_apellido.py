# Generated by Django 4.1.1 on 2022-10-07 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Veterinaria", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="veterinario",
            name="apellido",
        ),
    ]
