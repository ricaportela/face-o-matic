# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-06 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(blank=True, upload_to='carometro/'),
        ),
    ]
