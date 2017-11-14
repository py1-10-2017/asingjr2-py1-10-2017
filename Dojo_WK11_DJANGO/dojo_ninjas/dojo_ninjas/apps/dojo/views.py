# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

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
    context = {
        'color':request.session['color']
    }
    try:
        return render(request, 'dojo/show.html', context)
    except:
        pass
