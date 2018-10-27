# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-07 17:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now, verbose_name='published date'),
        ),
    ]