# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-20 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_auto_20170920_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_id',
            name='drop',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='request_id',
            name='pickup',
            field=models.DateTimeField(null=True),
        ),
    ]
