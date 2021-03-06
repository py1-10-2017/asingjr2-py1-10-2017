# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='secret_santa.BaseModel')),
            ],
            bases=('secret_santa.basemodel',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='secret_santa.BaseModel')),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100)),
            ],
            bases=('secret_santa.basemodel',),
        ),
        migrations.AddField(
            model_name='list',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secret_santa.Profile'),
        ),
    ]
