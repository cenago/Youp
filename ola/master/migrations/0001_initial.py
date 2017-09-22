# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-19 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustDtil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('user_lastname', models.CharField(max_length=250)),
                ('user_add', models.CharField(max_length=250)),
                ('user_long', models.CharField(max_length=250)),
                ('user_lat', models.CharField(max_length=250)),
                ('Cust_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverDtil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('user_lastname', models.CharField(max_length=250)),
                ('user_add', models.CharField(max_length=250)),
                ('user_long', models.CharField(max_length=250)),
                ('user_lat', models.CharField(max_length=250)),
                ('Driver_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_time', models.DateTimeField(auto_now_add=True)),
                ('pickup', models.DateTimeField(auto_now_add=True)),
                ('drop', models.DateTimeField(auto_now_add=True)),
                ('Status', models.IntegerField(default=0)),
                ('Cust_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.CustDtil')),
                ('Driver_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.DriverDtil')),
            ],
        ),
    ]