# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-17 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0028_place_world'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='world',
        ),
        migrations.AddField(
            model_name='place',
            name='is_world',
            field=models.BooleanField(default=False, verbose_name="Is this place your 'World' in which all other locations "),
            preserve_default=False,
        ),
    ]
