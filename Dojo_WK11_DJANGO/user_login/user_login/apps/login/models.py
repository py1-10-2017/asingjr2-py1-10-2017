# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User Data: first: {}, last: {}, email: {}, age: {}, created: {}, updated: {}>".format(self.first_name, self.last_name, self.email_address, self.age, self.created_at, self.updated_at)

'''
Class needs
first_name
last_name
email_address
age
created_at
updated_At
'''