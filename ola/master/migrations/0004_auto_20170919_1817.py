# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-19 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20170919_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custdtil',
            name='user_lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='custdtil',
            name='user_long',
            field=models.IntegerField(default=0),
        ),
    ]