# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-17 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20170717_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='detail',
        ),
    ]
