# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_monthlyweatherbycity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='challenge',
        ),
        migrations.AddField(
            model_name='run',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='run',
            name='date',
            field=models.DateTimeField(verbose_name='Run date'),
        ),
    ]