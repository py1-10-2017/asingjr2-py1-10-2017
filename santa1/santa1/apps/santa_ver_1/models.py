# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
#CANNOT USE VALIDTORS UNLESS ON FORMS

class AllManager(models.Manager):
    def reg_val(self, postData):
        error={}
        if len(postData['alias']) <1 or len(postData['alias']) > 100:
            error['alias'] = 'Cannot be blank or more than 100 characters'
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = "Must be valid email"
        if len(postData['password']) <1 or len(postData['password']) > 100:
            error['password'] = 'Cannot be blank or more than 100 characters'
        return error

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AllManager()

    class Meta:
        abstract = True

class Profile(BaseModel):
    alias = models.CharField( max_length=255, unique=True)
    email = models.CharField( max_length=255, unique=True)
    password = models.CharField( max_length=100)

    def __unicode__(self):
        return 'Alias = {}, Email = {}'.format(self.alias, self.email)

    def built_lists(self):
        return 'You have created {} list(s)'.format(self.list_set().count())

class List(BaseModel):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='update name')
    gift_max = models.IntegerField( default=40)

    def __unicode__(self):
        return 'Creator Name = {}'.format(self.creator.alias)

    def members(self):
        return 'The list has {} members'.format(self.member_set().count())

class Member(BaseModel):
    member_list = models.ForeignKey(
        List, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField( max_length=200, default='unknown')
    telephone = models.CharField(max_length=10, default='1234567890')

    def __unicode__(self):
        return 'Name = {}, Email = {}'.format(self.full_name, self.email)

class List_Member(BaseModel):
    lists = models.ManyToManyField(List)
    members = models.ManyToManyField(Member)
