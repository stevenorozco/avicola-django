# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avicola', '0007_auto_20170312_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galpon',
            name='eventos',
        ),
    ]