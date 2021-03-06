# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0012_challenge_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='goal_date',
            field=models.DateField(verbose_name='Goal date'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='start_date',
            field=models.DateField(auto_now_add=True, verbose_name='Starting date'),
        ),
        migrations.AlterField(
            model_name='run',
            name='date',
            field=models.DateField(verbose_name='Run date'),
        ),
    ]
