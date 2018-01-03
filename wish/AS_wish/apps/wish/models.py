# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Profile(BaseModel):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_pw = models.CharField(max_length=200)
    date_hired = models.DateField()

    def __unicode__(self):
        return 'name = {} username = {}'.format(self.name, self.username)

class Item(BaseModel):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(Profile, related_name='added_items', on_delete=models.CASCADE)
    shoppers = models.ManyToManyField(Profile, related_name='shoppers')