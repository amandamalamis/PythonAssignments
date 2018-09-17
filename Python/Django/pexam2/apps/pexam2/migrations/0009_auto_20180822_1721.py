# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pexam2', '0008_job_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Job', to='pexam2.User'),
        ),
        migrations.AlterField(
            model_name='join',
            name='join_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Join', to='pexam2.Job'),
        ),
        migrations.AlterField(
            model_name='join',
            name='join_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Join', to='pexam2.User'),
        ),
    ]