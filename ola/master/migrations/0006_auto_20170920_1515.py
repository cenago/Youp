# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-20 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_auto_20170920_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_id',
            name='Driver_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.DriverDtil'),
        ),
    ]
