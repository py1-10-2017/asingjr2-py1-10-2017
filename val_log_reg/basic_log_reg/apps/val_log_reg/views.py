from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

#VIEWS

def index(request):
    print 'index view'
    return render(request, 'val_log_reg/index.html')

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
                    if key == 'email':
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
                    alias=request.POST['alias'],
                    email=request.POST['email'],
                    password=safe_pw,
                    confirm_password=safe_pw,
                    dob=request.POST['dob']
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
                    return redirect('/success')
                if not bcrypt.checkpw(request.POST['password'].encode(), try_user.password.encode()):
                    print 'password failed'
                    messages.warning(
                        request, 'Password does not match anything in records')
                    return redirect('/')
            except:
                return redirect('/')

def success(request):
    print 'success view'
    return render(request, 'val_log_reg/success.html')
