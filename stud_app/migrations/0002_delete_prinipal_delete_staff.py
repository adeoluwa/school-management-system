# Generated by Django 4.1.1 on 2022-10-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stud_app", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Prinipal",
        ),
        migrations.DeleteModel(
            name="Staff",
        ),
    ]
