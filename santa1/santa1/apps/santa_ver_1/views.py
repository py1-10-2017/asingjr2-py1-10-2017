# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import BaseModel, Profile, List, Member
from django.contrib import messages
from .models import *
from random import shuffle
import bcrypt
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):
    print 'index view'
    today = datetime.date.today()
    current_day = today.strftime('%A, %x')
    xmas = datetime.date(2017, 12, 25)
    context = {
    'today': current_day, 
    'xmas':xmas, 
    }
    return render(request, 'santa_ver_1/reg_or_log.html',context)

def reg(request):
    print 'index view'
    today = datetime.date.today()
    current_day = today.strftime('%A, %x')
    xmas = datetime.date(2017, 12, 25)
    context = {
    'today': current_day, 
    'xmas':xmas, 
    }
    return render(request, 'santa_ver_1/reg.html',context)

def log(request):
    print 'index view'
    today = datetime.date.today()
    current_day = today.strftime('%A, %x')
    xmas = datetime.date(2017, 12, 25)
    context = {
    'today': current_day, 
    'xmas':xmas, 
    }
    return render(request, 'santa_ver_1/log.html',context) 

def list_update(request, list_id):
    if request.method != 'POST':
        request.session['list_for_update_id'] = list_id
        request.session.modified = True
        try:
            list1 = List.objects.get(id=list_id)
            print list1 
        except:
            return redirect('/main')
        context = {
            'list':list1,
        }
        return render(request, 'santa_ver_1/list_show.html', context)

def view_members(request, list_id):
    list1 = List.objects.get(id=list_id)
    ll = List.objects.get(id=list_id)
    list1 = list1.member_set.all()
    try:
        context = {
            'll': ll,
            'list1': list1
        }
        return render(request, 'santa_ver_1/view_members.html', context )
    except:
        print 'members not showing'
        return redirect('/main')

def list_delete(request, list_id):
    try:
        print List.objects.all().count()
        list1 = List.objects.get(id=list_id)
        list1.delete()
        print List.objects.all().count()
        return redirect('/main')
    except:
        return redirect('/main')

    
def post(request):
    print 'post view'
    if request.POST['form-type'] == 'register':
        all_profiles_email = Profile.objects.all()
        for user in all_profiles_email:
            if user.email == request.POST['email']:
                messages.warning(request,'Email already in use')
        try:
            check = Profile.objects.reg_val(request.POST)
            if len(check) > 0:
                for key in check.keys():
                    status = True
                    if key == 'alias':
                        print 'alias'   
                        messages.warning(request, 'Username cannot be blank or more than 100 characters')
                        status = False
                    if key == 'email':
                        print 'email'
                        messages.warning(request, 'Email must be valid email')
                        status = False
                    if key == 'password':
                        print 'password'
                        messages.error(request, 'Password cannot be blank or more than 100 characters')
                        status = False
                    if status == False:
                        return redirect('/reg')
                    else:
                        pass
            Profile.objects.create(
                alias=request.POST['alias'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            return redirect('/log')
        except:
            'no profile created'
            return redirect('/reg')
    if request.POST['form-type'] == 'login':
        if Profile.objects.all().count() < 1:
            print 'User email not registered'
            return redirect('/')
        try:
            user = Profile.objects.get(email=request.POST['email'])
        except:
            messages.warning(request, 'No matching email registered')
            return redirect('/log')
        if request.POST['password'] == user.password:
            print 'login successful'
            request.session['alias'] = user.alias
            request.session['user_id'] = user.id
            return redirect('/main')
        if request.POST['password'] != user.password:
            messages.warning(request, 'Password is incorrect')
            return redirect('/log')
    if request.POST['form-type'] == 'list':
        print 'trying to create list'
        print request.POST
        try:
            lists = List.objects.all()
            for thing in lists:
                if thing.name == request.POST['list_name']:
                    messages.warning(request, 'List name already in use')
                    return redirect('/main')
            if len(request.POST['list_name']) <1:
                messages.warning(request, 'List name cannot be blank')
            if int(request.POST['gift_max']) > 1000:
                messages.warning(request, 'Gift max cannot exceed 1000 dollars')
                return redirect('/main')
            List.objects.create(
            creator = Profile.objects.get(id = request.session['user_id']),
            name = str(request.POST['list_name']).upper(), 
            gift_max = request.POST['gift_max']
            )
            print 'list created'
            return redirect('/enter_members')
        except:
            print 'something went wrong'
            return redirect('/main')
    if request.POST['form-type'] == 'members':
        status = True
        list2 = List.objects.last().member_set.all()
        for member in list2:
            if member.email == request.POST['email']:
                messages.warning(request, 'Email already in use')
                status = False
        if len(request.POST['full_name']) < 1 or len(request.POST['full_name']) > 100:
            messages.warning(request, 'Member name cannot be blank or more than 100 characters')
            status = False
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.warning(request, 'Must be valid email')
            status = False
        if len(request.POST['telephone']) != 10:
            messages.warning(request, 'Telephone must be 10 digits')
            status= False
        if status != True:
            return redirect('/enter_members')

            full_name = request.POST['full_name']
            email = request.POST['email']
            print full_name, email

        # def add_member():
        try:
            Member.objects.create(
                member_list=List.objects.last(),
                    full_name=request.POST['full_name'],
                    email=request.POST['email'],
                    telephone=request.POST['telephone']
            )
            print 'member addded'
            return redirect('/enter_members')
        except:
            print 'no member created'
            return redirect('/enter_members')
        # if 'member_info' in request.session:
        #     add_member()
        #     print 'current members', request.session['member_info']
        #     request.session['member_info'].update(
        #         {request.POST['full_name']: request.POST['email']})
        #     request.session.modified = True
        #     print 'updated members', request.session['member_info']
        # else:
        #     add_member()
        #     request.session['member_info'] = {full_name: email}
        #     print request.session['member_info']
        # return redirect('/enter_members')
    if request.POST['form-type'] == 'list-update':
        print 'trying to update list'
        if 'list_for_update_id' in request.session:
            ulist = List.objects.get(id= request.session['list_for_update_id'])
            try:
                print 'name and max are', ulist.name, ulist.gift_max 
                ulist.name = request.POST['list_name']
                ulist.gift_max = request.POST['gift_max']
                ulist.save()
                print 'name and max are', ulist.name, ulist.gift_max 
                print 'list updated'
                return redirect('/main')
            except:
                print 'something went wrong'
                return redirect('/main')
        else:
            return redirect('/main')
    if request.POST['form-type'] == 'add-member':
        print 'post add member'
        try:
            Member.objects.create(
                member_list= List.objects.get(id=request.session['temp_id']), full_name=request.POST['full_name'],
                email=request.POST['email'],
                telephone=request.POST['telephone']
            )
            print 'member added'
            return redirect('/main')
        except:
            print'no one added'
            return redirect('/main')

def main(request):
    print 'main view'
    user = Profile.objects.get(id=request.session['user_id'])
    user_lists = user.list_set.all()
    if user_lists.count() == 0:
        print 'no lists created yet'
        context = {
        'user': user,
        }
        return render(request, 'santa_ver_1/main.html', context)
    else:
        print 'user has stored lists'
        context = {
            'user': user,
            'user_lists' : user_lists
        }
        return render(request, 'santa_ver_1/main.html', context)

def enter_members(request):
    print 'enter members view'
    list1 = List.objects.last()
    context = {
        'list_name': list1.name,
        'member_count': list1.member_set.all().count(),
        'current_members': list1.member_set.all(),
    }
    return render(request, 'santa_ver_1/enter_members.html', context)
    # if 'member_info' in request.session:
    #     # print 'member info exists'
    #     # context = {
    #     # 'list_name': list1.name,
    #     # 'len': len(list1.member_set.all())
    #     # }
    #     # return render(request, 'santa_ver_1/enter_members.html', context)
    #     pass
    # else:
    #     print 'no member info'
    #     context = {
    #         'list_name': request.session['list_name'],
    #         'current_members': list1.member_set.all(),  
    #         }
    #     return render(request, 'santa_ver_1/enter_members.html', context)

def add_member(request, list_id):
    print 'awesome'
    request.session['temp_id'] = list_id
    list1 = List.objects.get(id=list_id)
    return render(request, 'santa_ver_1/add_new_member.html', )
    if request.POST != 'POST':
        try:
            context = {
                'list':list1,
            }
        except:
            print 'nothing tried'
            return redirect('/main')
    if request.method == 'POST':
        print 'trying to add member'
        try:
            print 'member added'
            Member.objects.create(
                member_list = List.objects.get(id=request.session['temp_id']),
                full_name = request.POST['full_name'], 
                email = request.POST['email'], 
                telephone = request.POST['telephone']
            )
            return redirect('/main')
        except:
            print'no one added'
            return redirect('/main')

def ss_list(request, list_id):
    print 'ss_list view'
    list1 = List.objects.get(id=list_id)
    list_mem = List.objects.get(id=list_id).member_set.all()
    request.session['ss_list_members'] = []
    for mem in list_mem:
        request.session['ss_list_members'].append(mem.full_name)
    
    def secret_santa(member_list):
        new_list = member_list[:]
        print 'new list current', new_list
        shuffle(new_list)
        print 'new list jum', new_list

        results = {}
        for i, person in enumerate(new_list):
            try:
                results[person] = new_list[i+1]
            except IndexError:
                results[person] = new_list[0]
        print results
        return results

    request.session['ss_list_jumbled'] = secret_santa(request.session['ss_list_members'])
    context = {
        'list':list1,
        'ss_mem': request.session['ss_list_members'],
        'ss_mem_jum': request.session['ss_list_jumbled']
    }
    return render(request, 'santa_ver_1/ss_list.html', context)


def logout(request):
    print 'logout view'
    request.session.clear()
    return redirect('/')
