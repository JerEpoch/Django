# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amiibo', '0003_remove_amiibo_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibo',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
