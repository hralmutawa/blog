# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-10 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20171010_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(),
        ),
    ]
