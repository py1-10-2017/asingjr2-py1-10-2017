# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import Name_Form

# Create your views here.
def index(request):
    print 'index view'
    form = Name_Form()
    return render(request, 'sim_form/form.html', {'form':form})

def post(request):
    print 'post view'
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/display')

def display(request):
    print 'display view'
    print request.session
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment']
    }
    return render(request, 'sim_form/display.html', context)