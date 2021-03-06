# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-29 04:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0013_auto_20180928_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='tut_downvotes',
        ),
        migrations.AddField(
            model_name='tutor',
            name='tut_downvotes',
            field=models.ManyToManyField(blank=True, related_name='downs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='tut_upvotes',
        ),
        migrations.AddField(
            model_name='tutor',
            name='tut_upvotes',
            field=models.ManyToManyField(blank=True, related_name='ups', to=settings.AUTH_USER_MODEL),
        ),
    ]
