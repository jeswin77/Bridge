# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-29 04:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20180929_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor_likes',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='tutor_likes',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tutor_likes',
        ),
    ]
