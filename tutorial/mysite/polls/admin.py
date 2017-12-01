# -*- coding: utf-8 -*-
#**********************************************
#REALLY EASY
#**********************************************
from __future__ import unicode_literals
from django.contrib import admin
from .models import Question            
#MUST IMPORT MODEL BEFORE IT CAN BE USED
# Register your models here.

admin.site.register(Question)