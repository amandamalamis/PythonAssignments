# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-17 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pexam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default='description of wish', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='wish',
            field=models.CharField(default='wish', max_length=100),
            preserve_default=False,
        ),
    ]