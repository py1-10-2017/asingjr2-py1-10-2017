# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['first']) < 2:
            error['first'] = "First too short"
        if len(postData['last']) < 2:
            error['last'] = "Last name too short"
        if not EMAIL_REGEX.match(request.form['email']):
            error['email'] = "Email does not match valid email"
        if len(postData['password']) < 8:
            error['password'] = "Password too short"
        if len(postData['confirm_password']) != postData['password']:
            error['confirm_password'] = "Confirm password does not match password"
        return error

class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()