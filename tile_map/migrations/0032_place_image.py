# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-17 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0031_auto_20170717_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
