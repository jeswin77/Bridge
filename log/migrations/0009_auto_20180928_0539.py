# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_auto_20180928_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='tut_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/tutorpics'),
        ),
    ]
