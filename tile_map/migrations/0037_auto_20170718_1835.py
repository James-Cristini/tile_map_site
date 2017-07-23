# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-18 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0036_auto_20170718_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='associated_tiles',
            field=models.ManyToManyField(blank=True, null=True, to='tile_map.Tile'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='locations',
            field=models.ManyToManyField(blank=True, null=True, to='tile_map.Place'),
        ),
    ]