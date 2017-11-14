# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    try:
        return HttpResponse('Home page')
    except:
        pass

def show(request):
    try:
        return HttpRespnse('Show Page')
    except:
        pass