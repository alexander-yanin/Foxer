# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 07:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authsys', '0002_auto_20170202_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='/')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsys.User')),
            ],
        ),
    ]
