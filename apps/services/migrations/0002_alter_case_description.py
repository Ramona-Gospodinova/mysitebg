# Generated by Django 5.1.5 on 2025-01-28 07:37

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
