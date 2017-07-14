# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-14 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0020_tile_organizations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tile',
            options={'ordering': ('title',)},
        ),
        migrations.AlterField(
            model_name='place',
            name='tiles',
            field=models.ManyToManyField(blank=True, to='tile_map.Tile'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='organizations',
            field=models.ManyToManyField(blank=True, to='tile_map.Organization'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='tradegoods',
            field=models.ManyToManyField(blank=True, to='tile_map.Tradegood'),
        ),
    ]
