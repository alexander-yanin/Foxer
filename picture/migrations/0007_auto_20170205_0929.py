# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0006_remove_picture_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='picture',
            name='key_words',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
