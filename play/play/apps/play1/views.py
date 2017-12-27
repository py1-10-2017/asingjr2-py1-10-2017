from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
import random
from .forms import ProfileForm, PlayForm
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login

#Creating index with a new user being created everytime
def index(request):
    print 'index view'
    User.objects.create(first_name='Frank', last_name='Tank', username= str(random.randint(0,100)))
    testuser = authenticate(first_name=request.POST['first_name'],last_name=request.POST['last_name'], username=request.POST['username'])
    users = User.objects.all()
    return render(request, 'play1/index.html', {'users':users})

def form(request):
    print 'form view'
    print 'non post route'
    form1 = ProfileForm() 
    form2 = PlayForm()
    context = {
        'form1':form1,
        'form2':form2 
    }
    return render(request, 'play1/forms.html',context)

def test(request):
    if request.method == 'POST':
        print 'post route'
        bound_form = ProfileForm(request.POST)
        print 'is valid test', bound_form.is_valid
        print 'errors', bound_form.errors
        return redirect('/form')
    
def post(request):
    print 'post view'
    return redirect('/')

#Import option to return 404 or simply use try and except statement...other option is if statement or while statement
def param_test(request, param):
    print 'param test view'
    #EASY SHORTCUT FOR PULLING OBJECT..other options is to just use try and except
    if param < 3:
        profile_number = get_object_or_404(Profile, pk=param)
        context = {
            'param': param,
            'profile_number':profile_number
        }
        return render(request, 'play1/param_test.html', context)
    else:
        try:
            profile_number = Profile.objects.get(id = param)
            context = {
                'param': param,
                'profile_number': profile_number
            }
            return render(request, 'play1/param_test.html', context)
        except:
            context = {
                'param': param,
            }
            return render(request, 'play1/param_test.html', context)


def logout(request):
    print 'logout view'
    return redirect('/')
