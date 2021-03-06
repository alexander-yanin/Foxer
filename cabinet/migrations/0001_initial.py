# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('picture', '0015_auto_20170210_1809'),
        ('authsys', '0005_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ManyToManyField(to='picture.Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authsys.User')),
            ],
        ),
    ]
