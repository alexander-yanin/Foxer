# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartsys', '0004_auto_20170210_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authsys.User'),
        ),
    ]
