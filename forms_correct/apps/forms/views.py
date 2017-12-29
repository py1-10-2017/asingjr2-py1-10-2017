# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import ProfileForm, FamilyForm, PForm, ProfileForm2
from django.contrib import messages

def index(request):
    print 'index view'
    form1 = ProfileForm() 
    form2 = PForm()
    form3 = ProfileForm2
    context = {
        'form1': form1,
        'form2': form2, 
        'form3':form3
    }
    return render(request,'forms/index.html', context)

def post(request):
    print 'post view'
    if request.method == 'POST':
        if request.POST['type'] == 'model':
            print 'model form'
            try:
                form = ProfileForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    print 'model form is not valid'
            except:
                print 'no model creation tried', form.errors


        if request.POST['type'] == 'form':
            print 'form form'
            try:
                form = PForm(request.POST)
                print 'is form valid', form.is_valid()
                print form['age'].clean()
                print 'form clean dict', form.cleaned_data
                print 'form errors', form.errors
                print 'form created with form form', form.errors
   
            except:
                print 'didnt try form profile process'
                print 'form errors', form.errors
                
        if request.POST['type'] == 'manual':
            print 'manual form'
            try:
                Profile.objects.create( 
                    first=request.POST['first'],
                    last = request.POST['last'],
                    age = request.POST['age'],
                    email = request.POST['email'],
                    telephone = request.POST['telephone']
                )
                print 'model created with manual form'
            except:
                print 'could not create manual profile'
    return redirect('/')


    return redirect('/')

def display(request):
    print 'display view'
    return HttpResponse('display ')

def index2(request):
    print 'index2 page'
    form = MovieForm()
    context = {
        'form':form
    }
    return render(request, 'forms/new.html',context)

def new_post(request):
    print 'new post view'
    form = MovieForm(request.POST)
    try:
        print 'try test'
        print 'is form valid', form.is_valid()
        if form.is_valid() == True:
            form.save() 
        else:
            messages.warning(request, 'SOMETHING WENT WRONG')
            print 'error in form', form.errors
    except:
        print 'no test tried'
    return redirect('/')