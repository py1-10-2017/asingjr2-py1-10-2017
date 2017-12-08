# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(BaseModel):
    alias = models.CharField(max_length=255, unique = True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    def __unicode__(self):
        return 'Alias = {}, Email = {}'.format(self.alias, self.email) 

class List(BaseModel):
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length = 255, default='update name')
    def __unicode__(self):
        return 'Creator Name = {}'.format(self.creator.alias)

class Member(BaseModel):
    lists = models.ManyToManyField(List)    #Move to sepaate page to create list
    full_name = models.CharField(max_length =255)
    email = models.CharField(max_length=200, default='unknown')
    telephone = models.BigIntegerField(default=1234567890)
    def __unicode__(self):
        return 'Name = {}, Email = {}'.format(self.full_name, self.email)


    