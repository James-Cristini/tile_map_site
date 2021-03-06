# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-12 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0015_auto_20170712_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='tile',
            field=models.CharField(default='Tile 1', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='location',
            field=models.CharField(default='Eleros', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='organization_1',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='organization_2',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='tradegood_1',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='tradegood_2',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='tradegood_3',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='place',
            name='parent_location',
            field=models.CharField(max_length=55),
        ),
    ]
