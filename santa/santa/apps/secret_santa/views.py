# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import BaseModel, List, Member, Profile
import datetime

def index(request):
    print 'index view'
    return render(request, 'secret_santa/index.html')

def post(request):
    print 'post view'
    if request.method == 'POST':
        if request.POST['form-type'] == 'register':
            try:
                Profile.objects.create(
                alias = request.POST['alias'],
                email = request.POST['email'],
                password = request.POST['email']
                )
                print 'Profile created'
                return redirect('/')
            except:
                'no profile created'
                return redirect('/')
        if request.POST['form-type'] == 'login':
            if Profile.objects.all():
                user = Profile.objects.get(email = request.POST['email'])
            else:
                print 'no profiles yet'
                return redirect('/')
            request.session['alias'] = user.alias
            request.session['id'] = user.id
            print request.session['id']
            if request.POST['password'] == user.password:
                print 'login succesful'
                return redirect('/main')
            if request.POST['password'] != user.password:
                print 'login unsuccessful'
                return redirect('/')
        if request.POST['form-type'] == 'secret_santa':
            request.session['initial_members'] = request.POST['initial_members']
            request.session['list_name'] = request.POST['list_name']
            return redirect('/enter_members')

def main(request):
    print 'main view'
    today = datetime.date.today()
    current_day = today.strftime('%A, %x')
    user = Profile.objects.get(id = request.session['id'])
    context = {
        'user':user,
        'today': current_day
    }
    return render(request, 'secret_santa/main.html', context)

def enter_members(request):
    print 'enter members view'
    print request.session['initial_members']
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        if 'member_info' in request.session:
            request.session['member_info'].update( {full_name:email} )
            print 'member info updated'
            return redirect('/enter_members')
        else:
            request.session['member_info'] = {full_name:email}
            print 'member info established'
            return redirect('/enter_members')
    if request.method != 'POST':
        if 'member_info' in request.session:
            context = {
                'list_name': request.session['list_name'],
                'current_members': request.session['member_info']
            }
            return render(request, 'secret_santa/enter_members.html', context)
        else: 
            context = {'list_name': request.session['list_name']}
            return render(request, 'secret_santa/enter_members.html', context)
    
def play(request):
    print 'play view'
    return render(request, 'secret_santa/play.html')

def play2(request):
    print 'play view'
    return render(request, 'secret_santa/play2.html')

def logout(request):
    print 'logout view'
    request.session.clear()
    return redirect('/')

#Need to flesh out page with logic
