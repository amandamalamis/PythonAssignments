# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pexam2', '0009_auto_20180822_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='join_job',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='join',
            old_name='join_user',
            new_name='user',
        ),
    ]