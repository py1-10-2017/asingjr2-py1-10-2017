# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if request.method ='POST':
        errors = User.objects.basic_validator(request.POST)
        try:
            if len(errors) > 0:
                print "failed validatation"
                for key, message in errors.iteritems():
                    print key, message
                return redirect('/')
            else:
                return redirect('/success')
        except:
            return redirect('/')

    return HttpResponse('Home')

def success(request):
    return HttpResponse('Successfully Logged')
