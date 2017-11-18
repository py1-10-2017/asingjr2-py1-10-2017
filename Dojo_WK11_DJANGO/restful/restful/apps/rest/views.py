# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print 'At index view'
    users = User.objects.all()  # Query will not work without importing entire file
    context = {
        'users': users
    }
    return render(request,'index.html', context)

def new(request):
    print "At new view"
    return render(request, 'new.html')

def post_new(request):
    print 'At post_new view'
    print 'Created new user'
    print request.POST
    User.objects.create(
        first=request.POST['first'],
        last=request.POST['last'], 
        email=request.POST['email']) #Need to check in multiple spacing will be issue
    return redirect('/')
    pass 

def display(request, user_id):  #Displaying using id
    context = {
    'user': User.objects.get(id=user_id)
    }
    print user_id
    return render(request, 'display.html', context)

def update(request, user_id):
    context = {
    'user': User.objects.get(id=user_id)
    }
    print user_id
    print 'At update view'
    return render(request, 'update.html', context)

def post_update(request, user_id):
    print "at post_update view"
    try:
        user = User.objects.get(id=user_id)
        user.first=request.POST['first']
        user.last = request.POST['last']
        user.email = request.POST['email']
        user.save()
        print 'user updated'
        return redirect('/')  
    except:
        print 'not updated'
        pass 

def delete(request, user_id):
    print 'At delete view'
    print user_id
    try:
        rm_user = User.objects.get(id=user_id)
        rm_user.delete()
        print 'user deleted'
        return redirect('/')
    except:
        print 'user not delete'
        return redirect('/')
    

#  NEED TO ADD ALL CONTEXT FOR RENDERING
