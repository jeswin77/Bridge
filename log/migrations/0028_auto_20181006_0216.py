# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-06 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0027_auto_20181006_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='tut_course',
        ),
        migrations.AddField(
            model_name='tutor',
            name='tut_course',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to='log.Category'),
        ),
    ]
