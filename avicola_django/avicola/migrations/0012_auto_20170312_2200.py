# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avicola', '0011_remove_gallina_novedad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lote',
            name='galpon',
        ),
        migrations.AddField(
            model_name='gallina',
            name='galpon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='avicola.Galpon'),
            preserve_default=False,
        ),
    ]
