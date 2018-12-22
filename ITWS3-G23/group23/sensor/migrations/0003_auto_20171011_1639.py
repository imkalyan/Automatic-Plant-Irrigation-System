# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_auto_20171009_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='humidity',
            name='timeanddate',
            field=models.CharField(default=56, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soilmoisture',
            name='timeanddate',
            field=models.CharField(default=45, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperature',
            name='timeanddate',
            field=models.CharField(default=23, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterlevel',
            name='timeanddate',
            field=models.CharField(default=89, max_length=250),
            preserve_default=False,
        ),
    ]
