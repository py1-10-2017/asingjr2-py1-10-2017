# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime             #added late in tutorial
from django.utils import timezone           #research utils and timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return u'question text is = {}'.format(self.question_text)
    #included unicode to allows for display of other types of characters vs string
    #in python 3 __str__ method is used

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    #added default for votes field
    def __str__(self):
        return self.choice_text
#**********************************************************************************************
#adding related name removes option for "choice_set.all() and is replaced by choices.all()"
#***************************************************************************************