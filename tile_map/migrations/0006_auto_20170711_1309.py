# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-11 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0005_culture_food_organization_person_place_workofart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='descrption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='person',
            name='occupation',
            field=models.CharField(max_length=50),
        ),
    ]