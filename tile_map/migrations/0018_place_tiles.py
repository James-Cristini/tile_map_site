# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-13 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0017_auto_20170713_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='tiles',
            field=models.ManyToManyField(to='tile_map.Tile'),
        ),
    ]
