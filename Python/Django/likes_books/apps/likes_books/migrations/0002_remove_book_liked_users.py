# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-13 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='liked_users',
        ),
    ]