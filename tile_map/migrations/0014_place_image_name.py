# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-12 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0013_auto_20170712_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image_name',
            field=models.CharField(default='placeholder', max_length=75),
            preserve_default=False,
        ),
    ]
