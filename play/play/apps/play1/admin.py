# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import BaseModel, Profile, Color


class ProfileAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'age')

class ColorAdmin(admin.ModelAdmin):
    fields = ('name', 'family','profile')
    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Color, ColorAdmin)
