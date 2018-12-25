# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-25 21:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0002_auto_20181226_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='project',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
