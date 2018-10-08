# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-06 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0029_auto_20181006_0218'),
        ('tutor', '0014_auto_20181006_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='tutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='log.Tutor'),
            preserve_default=False,
        ),
    ]