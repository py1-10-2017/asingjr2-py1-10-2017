# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    class_name = models.CharField(max_length=100)
    def __str__(self):
        return "class_name {}".format(self.class_name)

class Student(models.Model):
    name = models.CharField(max_length= 100)
    courses = models.ManyToManyField(Course, related_name='students')
    def __str__(self):
        return "name {}".format(self.name)
