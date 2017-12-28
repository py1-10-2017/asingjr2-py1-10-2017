# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 03:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play1', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(6, message='Need more characters my friend')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]