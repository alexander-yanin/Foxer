# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
