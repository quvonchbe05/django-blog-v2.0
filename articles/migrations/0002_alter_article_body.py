# Generated by Django 4.1.5 on 2023-01-10 04:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="body",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
