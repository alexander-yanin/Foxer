# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_auto_20170203_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, upload_to='picture/static/picture/'),
        ),
    ]
