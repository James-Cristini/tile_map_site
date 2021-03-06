# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-19 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0037_auto_20170718_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='associated_tiles',
            field=models.ManyToManyField(blank=True, to='tile_map.Tile'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='locations',
            field=models.ManyToManyField(blank=True, to='tile_map.Place'),
        ),
        migrations.AlterField(
            model_name='person',
            name='locations',
            field=models.ManyToManyField(to='tile_map.Place'),
        ),
    ]
