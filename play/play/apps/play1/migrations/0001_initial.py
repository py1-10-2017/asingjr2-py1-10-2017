# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-23 02:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(validators=[django.core.validators.MaxLengthValidator(15, message='Cannot be longer than 15 characters')])),
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
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message="Brolly's email is stronger"), django.core.validators.MinLengthValidator(6, message='Need more characters my friend')])),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(75, message='Cannot be older than 75'), django.core.validators.MinValueValidator(21, message='Must be at least 21')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='color',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play1.Profile'),
        ),
    ]