# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-08 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tile_map', '0003_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='question_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
