# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
