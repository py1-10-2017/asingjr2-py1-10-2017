# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
