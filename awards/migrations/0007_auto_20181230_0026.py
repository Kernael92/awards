# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-29 21:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_project_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]