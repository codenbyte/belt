# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default='', max_length=45),
        ),
    ]
