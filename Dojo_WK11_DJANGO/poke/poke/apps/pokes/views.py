# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if 'name' in request.session:
        request.session.flush()
    print 'index view'
    return render(request, 'pokes/index.html')

def post(request):
    print 'post view'
    if request.method == 'POST':
        if request.POST['form_type'] == 'register':
            print request.POST
            print 'running check'
            check = User.objects.registration_validation(request.POST)
            if len(check) > 0:
                for key, message in check.iteritems():
                    if key == 'name':
                        messages.warning(
                            request, 'Name must be at least 3 characters')
                    if key == 'alias':
                        messages.warning(
                            request, 'Alias must be at least 3 characters')
                    if key == 'email' :
                        messages.warning(request, 'email is not valid')
                    if key == 'password':
                        messages.warning(
                            request, 'Password must be at least 8 characters')
                    if key == 'confirm_password':
                        messages.warning(request,
                                            'Password field and confirm password field must match')
                    print key, message
                    return redirect('/')
            else:
                safe_pw = bcrypt.hashpw(
                    request.POST['password'].encode(), bcrypt.gensalt())
                User.objects.create(
                    name=request.POST['name'],
                    alias = request.POST['alias'],
                    email=request.POST['email'],
                    password=safe_pw,
                    confirm_password=safe_pw,
                    dob = request.POST['dob']
                )
                print 'user created'
                test = User.objects.all()
                print 'users so far = ', test.count()
                print 'last user = ', User.objects.last()
                return redirect('/')
        if request.POST['form_type'] == 'login':
            print request.POST
            try_user = User.objects.get(email=request.POST['email'])
            try:
                if bcrypt.checkpw(request.POST['password'].encode(), try_user.password.encode()):
                    print 'password matches'
                    request.session['name'] = try_user.name
                    request.session['email'] = try_user.email
                    request.session['user_id'] = try_user.id
                    for k, v in request.session.iteritems():
                        print k, v
                    return redirect('/home')
                if not bcrypt.checkpw(request.POST['password'].encode(), try_user.password.encode()):
                    print 'password failed'
                    messages.warning(request, 'Password does not match anything in records')
                    return redirect('/')
            except:
                return redirect('/')


def home(request):
    print "home view"
    print request.session['name']
# Poke Logic
    logged_user = User.objects.get(id = request.session['user_id'])
    au = User.objects.all()
    print 'logged user is ',logged_user
    pokes_set = logged_user.pokes.all() 
    print pokes_set
    poke_attempts = logged_user.poke_attempts.all()
    print poke_attempts
    context = {
        'au': au,
        'lu': logged_user, 
        'pokes_set': pokes_set,
        'poke_attempts': poke_attempts
    }
    return render(request, 'pokes/home.html', context)

def poke_post(request):
    print 'post poke view'
    utp = User.objects.get(id=request.POST['user_to_poke'])
    logged_user = User.objects.get(name=request.session['name'])
    Poke_Attempt.objects.create(
        user_poked = utp, 
        poker = logged_user    
    )
    print 'poke try successful'
    print 'last poke attempt info = ', Poke_Attempt.objects.last()
    return redirect('/home')
  
def logout(request):
    print 'logout view'
    request.session.flush()
    return redirect('/')

