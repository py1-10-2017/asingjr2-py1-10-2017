# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models 
from django.template import loader

from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    request.session['day'] = 'today'
    print request.session['day']
    try:
        return HttpResponse('Home Page')
    except:
        pass

def show(request):
    print 'moved to show page'
    request.session['color'] = 'red'
    print request.session['color']

    all_dojos = Dojos.objects.get(id=1)
    all_ninjas = Ninjas.objects.all()
    context = {
        'color':request.session['color'], 
        'Dojos': all_dojos,
        'Ninjas':all_ninjas
    }
    try:
        return render(request, 'dojo/show.html', context)
    except:
        pass
