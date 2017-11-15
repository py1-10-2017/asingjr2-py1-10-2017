# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=10)
    print "Dojos object/record succesfully created"
    def __str__(self):
        return "<Blog Info: DOJO: {}, CITY: {}, STATE: {}>".format(self.name, self.city, self.state)
    
class Ninjas(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    color = models.CharField(default='red', max_length=100)
    day = models.CharField(max_length = 50)
    dojo = models.ForeignKey(Dojos, related_name="ninjas")
    print "Ninjas object/record succesfully created"
    def __str__(self):
        return "<Blog Info: First: {}, Last: {}>".format(self.first_name, self.last_name)
