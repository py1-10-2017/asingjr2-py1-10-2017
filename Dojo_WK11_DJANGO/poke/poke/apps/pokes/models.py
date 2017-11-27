# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

class AllManager(models.Manager):
    def registration_validation(self, postData):
        error = {}
        if len(postData['name']) < 2:
            error['name'] = "Name too short"
        if len(postData['alias']) < 2:
            error['alias'] = "Username too short"
        if not EMAIL_REGEX.match(postData['email']):
            # MUST BE REFERENCED CORRECTLY
            error['email'] = "Email is not valid email"
        if len(postData['password']) < 2:
            error['password'] = 'Password must be at least 2 characters'
        if postData['confirm_password'] != postData['password']:
            error['confirm_password'] = "Confirm password does not match password"
        return error

class User(models.Model):
    name = models.CharField(max_length=200, default='person')
    alias = models.CharField(max_length=200, default='random_alias')
    email = models.CharField(max_length=200, default='random_email')
    password = models.TextField()
    confirm_password = models.TextField()
    dob = models.CharField(max_length =100, default = 'add dob')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AllManager()
    def __str__(self):
        return 'Name is {}, Email is {}'.format(self.name, self.email)


class Poke_Attempt(models.Model):
    user_poked = models.ForeignKey(User, related_name = 'pokes')
    poker = models.ForeignKey(User, related_name = 'poke_attempts')
    def __str__(self):
        return 'user poked = {} and poker was {}'.format(self.user_poked, self.poker)
