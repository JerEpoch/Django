# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-28 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0008_amiibo_gtotals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibo',
            name='gtotals',
            field=models.FloatField(default=0, max_length=6),
        ),
    ]