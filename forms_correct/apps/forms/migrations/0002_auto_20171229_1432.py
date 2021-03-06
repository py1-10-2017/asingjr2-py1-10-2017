# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 19:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, message='value too shoooooooort')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(default='915', max_length=10),
        ),
    ]
