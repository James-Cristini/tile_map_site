# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-12 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0011_auto_20170712_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='location',
            field=models.CharField(default='Eleros', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='location',
            field=models.CharField(default='Eleros', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tradegood',
            name='location',
            field=models.CharField(default='Eleros', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workofart',
            name='location',
            field=models.CharField(default='Eleros', max_length=50),
            preserve_default=False,
        ),
    ]
