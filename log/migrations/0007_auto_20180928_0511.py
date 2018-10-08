# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_auto_20180928_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='tut_locality',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tut_rate',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tut_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
