# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse 
from .models import Profile, Item 
from .forms import RegisterForm, ItemForm
import bcrypt 
from django.contrib import messages 

def index(request):
    print 'index view'
    if 'user_id' in request.session:
        print 'session is live'
    form =RegisterForm()
    context ={
        'form':form
    }
    return render(request, 'wish/index.html', context)

def post(request):
    print 'post view'
    print request.POST
    warnings_dict = {
        'name':'Name must contain "aa"', 
        'username': 'Username must be at least 2 characters',
        'password': 'Password must be at least 2 characters',
        'confirm_pw': 'Password does not match anything in records',
        'date_hired':'Date hired does not match anything in records',
        'login_password': 'Password does not match anything in records',
        'login_username': 'Username does not match anything in records',
    }
    form = RegisterForm(request.POST)
    if request.POST['form-type'] == 'register':
        if form.is_valid():
            print 'clean dict', form.cleaned_data
            if request.POST['confirm_pw'] != request.POST['password']:
                messages.warning(
                    request, 'Password does not match Confirm Password')
            safe_pw = bcrypt.hashpw(
                form.cleaned_data['password'].encode(), bcrypt.gensalt())
            Profile.objects.create(
                name=form.cleaned_data['name'],
                username=form.cleaned_data['username'],
                password=safe_pw,
                confirm_pw=form.cleaned_data['confirm_pw'],
                date_hired= request.POST['date_hired']
            )
            print 'profile created'
            return redirect('/')
        if len(form.errors) > 0: 
            print 'form errors are', form.errors
            for k, v in warnings_dict.iteritems():
                if k in form.errors:
                    messages.warning(request, v)
            return redirect('/')
        
    if request.POST['form-type'] == 'login':
        print 'trying login'
        print request.POST
        try:
            try:
                try_user = Profile.objects.get(username=request.POST['username'])
            except:
                messages.warning(
                    request, message_dict['login_username'])
            if bcrypt.checkpw(request.POST['password'].encode(),    try_user.password.encode()):
                print 'password matches'
                request.session['name'] = try_user.name
                request.session['username'] = try_user.username
                request.session['user_id'] = try_user.id
                request.session['rem'] = []
                return redirect('/main')
            if not bcrypt.checkpw(request.POST['password'].encode(), try_user.password.encode()):
                messages.warning(
                    request, message_dict['login_password'])
                return redirect('/')
        except:
            return redirect('/')

    if request.POST['form-type'] == 'add_item':
        print 'add item post'
        if len(request.POST['name']) < 4:
            messages.warning(request,"Name of item/product must be at least 3 characters")
            return redirect('/new')
        else:
            form = ItemForm(request.POST)
            if form.is_valid():
                user = Profile.objects.get(id=request.session['user_id'])
                Item.objects.create(
                    name=request.POST['name'],
                    added_by = user 
                )
                print 'item created'
                item = Item.objects.last()
                item = item.shoppers.add(user)
                return redirect('/main')
            else:
                print 'something happened'
                return redirect('/new')
        
        return HttpResponse('post')

def main(request):
    print 'main view'
    print 'rem = ', request.session['rem']
    user = Profile.objects.get(id = request.session['user_id'])
    wish_list = Item.objects.filter(shoppers__id= user.id).exclude(id__in=request.session['rem'])
    nums = []
    for thing in wish_list:
        nums.append(thing.id) 
    print nums
    all_items = Item.objects.all().exclude(id__in=nums)
    context = {
        'user':user,
        'wish_list': wish_list,
        'all_items':all_items
    }
    return render(request, 'wish/main.html', context)

def new(request):
    print 'new view'
    form = ItemForm()
    profiles = Profile.objects.all()
    items = Item.objects.all()
    context = {
        'form':form, 
        'profiles': profiles, 
        'items': items,

    }
    return render(request, 'wish/new.html', context)

def add_to_wish(request, item_id):
    print 'add to wish view'
    user = Profile.objects.get(id=request.session['user_id'])
    item = Item.objects.get(id=item_id)
    item = item.shoppers.add(user)
    return redirect('/main')

def del_from_wish(request, item_id):
    print 'add to wish view'
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('/main')

def rem_from_wish(request, item_id):
    print 'rem from wish view'
    request.session['rem'].append(item_id)
    request.session.modified = True
    print request.session['rem']
    return redirect('/main')

def item(request, item_id):
    print 'item view'
    item = Item.objects.get(id=item_id)
    return render(request, 'wish/item.html', {'item':item})

def logout(request):
    print 'logout view'
    request.session.clear()
    return redirect('/')


