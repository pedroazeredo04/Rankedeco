# Generated by Django 4.2.6 on 2023-11-28 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ranking", "0009_alter_bandeco_img_url"),
    ]

    operations = [
        migrations.RemoveField(model_name="item", name="category",),
    ]
