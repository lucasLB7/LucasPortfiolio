# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='githuburl',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
