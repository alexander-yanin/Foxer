# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0002_auto_20170202_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
