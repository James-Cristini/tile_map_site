# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-12 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0009_person_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.CharField(default='Village', max_length=50),
            preserve_default=False,
        ),
    ]
