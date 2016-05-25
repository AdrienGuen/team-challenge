# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0009_auto_20160516_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='team',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
