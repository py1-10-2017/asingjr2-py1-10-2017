# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import BaseModel, Profile, List, Member
# Register your models here.

admin.site.register(Profile)
admin.site.register(List)
admin.site.register(Member)
