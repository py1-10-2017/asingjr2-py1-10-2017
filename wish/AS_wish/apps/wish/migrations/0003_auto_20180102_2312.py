# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0002_auto_20180102_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_items', to='wish.Profile'),
        ),
    ]
