# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-17 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0030_auto_20170717_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='rent_loc',
            new_name='parent_location',
        ),
    ]
