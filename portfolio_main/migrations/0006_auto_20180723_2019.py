# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0005_auto_20180711_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='media/project_images'),
        ),
    ]