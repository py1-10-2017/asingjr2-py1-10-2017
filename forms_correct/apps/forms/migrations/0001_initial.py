# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 03:15
from __future__ import unicode_literals

import apps.forms.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('Jones', 'JONES'), ('Harris', 'HARRIS'), ('Sings', 'SINGS'), ('Smiths', 'SMITHS')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first', models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Must be at least two characters'), django.core.validators.MaxLengthValidator(15, message='Must be at least two characters')])),
                ('last', models.CharField(max_length=200)),
                ('age', models.IntegerField(validators=[apps.forms.models.even, django.core.validators.MinLengthValidator(21, message='Must be between 21 and 100'), django.core.validators.MaxValueValidator(100, message='Must be between 21 and 100')])),
                ('email', models.EmailField(max_length=200, validators=[django.core.validators.EmailValidator])),
                ('telephone', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='family',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Profile'),
        ),
    ]
