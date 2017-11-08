# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    print 'At home page'
    print request.session
    return render(request, 'survey/index.html')

def submit(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['fav'] = request.POST['fav']
    request.session['comment'] = request.POST['comment']

    print request.POST
    print request.POST['name']
    print request.session['name'], request.session['location'], request.session['fav'], request.session['comment']
    print 'information submitted'
    print request.POST
    print request.method
    if request.method == "POST":
        print 'success'
        return redirect('/result')  
    else:
        print 'failure'
        return redirect('')
    
def result(request):
    context = {
        'counter': request.session['counter'],
        'name': request.session['name'],
        'location': request.session['location'],
        'fav': request.session['fav'],
        'comment': request.session['comment']
    }
    print 'result of info'
    print request.session['name']
    return render(request, 'survey/result.html', context)

def test(request):
    print 'temp check'
    return render(request, 'survey/result.html' )
