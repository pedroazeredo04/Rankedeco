# Generated by Django 4.2.6 on 2023-11-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ranking", "0006_alter_bandeco_contato_alter_bandeco_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bandeco",
            name="img_url",
            field=models.CharField(default="", max_length=255),
        ),
    ]
