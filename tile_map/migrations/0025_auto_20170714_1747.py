# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-14 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0024_auto_20170714_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='occupation',
            field=models.CharField(max_length=75),
        ),
    ]
