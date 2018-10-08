# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-06 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0025_auto_20181006_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='tut_course',
        ),
        migrations.AddField(
            model_name='tutor',
            name='tut_course',
            field=models.ManyToManyField(default=1, related_name='tutors', to='log.Category'),
        ),
    ]
