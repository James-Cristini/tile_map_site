# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-14 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0023_tile_related_places'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tile',
            old_name='related_places',
            new_name='relevant_places',
        ),
    ]
