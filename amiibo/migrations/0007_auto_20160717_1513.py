# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0006_amiibo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibo',
            name='price',
            field=models.FloatField(default=12.99, max_length=6),
        ),
    ]