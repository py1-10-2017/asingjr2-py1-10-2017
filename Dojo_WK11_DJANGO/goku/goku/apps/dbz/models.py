# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):           #Important to remember to add new manager for validation pieces
    name = models.CharField(max_length= 100)
    alias = models.CharField(max_length= 100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return "name : {}, alias: {}, email {}".format(self.name, self.alias, self.email)

class Author(models.Model):     #Will not need much information to start
    author_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "author: {},".format(self.author_name)

class Book(models.Model):           #Many side of one to many has foreign key
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, related_name='books')
    added_by = models.ForeignKey(User, related_name='user_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "title: {},".format(self.title)

class Review(models.Model):         #many side of one to many has foreign key
    review = models.CharField(max_length = 100)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews')
    reviewer = models.ForeignKey(User, related_name='review_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "review: {}, rating {}, book {}  reviewer{}".format(self.review, self.rating, self.book, self.reviewer)

class Student(models.Model):            #Did not meed much to start
    name = models.TextField()

class Course(models.Model):
    course_name = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)


class DSSN(models.Model):
    #DSN = Dog SSN number
    SSN = models.IntegerField()
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "DSSN number {} and color is {}".format(self.SSN, self.color)

class Dog(models.Model):
    DSSN = models.OneToOneField(DSSN, related_name='dog')



