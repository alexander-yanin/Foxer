# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0003_auto_20170204_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
