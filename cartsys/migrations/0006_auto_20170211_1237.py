# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartsys', '0005_auto_20170210_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsys.User'),
        ),
    ]
