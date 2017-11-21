# -*- coding: utf-8 -*-
'''
**************************************
IMPORTANT NOTES
Can do one post routes with differnt criteria for actions like hidden input with form type names;
Can create one to one, one to many, or many to many fields after original class has been created;
Can choose to create default value directly through models vice "makemigrations";
Queryset's are the only thing returned when accessing foreign keys!!!!;
Can do raw_sql or Q(question) for more direct lookups.
*********************************************************
'''

from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print 'index view'
    try:
        if 'name' in request.session:
            request.session.clear()
        print 'session cleared'
    except:
        print 'nothing to clear'
        pass
    return render(request, 'index.html')

def post(request):
    if request.method == 'POST':
        if request.POST['hidden'] == 'register':
            print 'register form'
            User.objects.create(
                name=request.POST['name'], 
                alias=request.POST['alias'], 
                email=request.POST['email'], 
                password=request.POST['password']
                )
            print 'Register success'
            return redirect('/')
        if request.POST['hidden'] == 'login':
            print 'login form'
            email_try = request.POST['email']
            log_user = User.objects.get(email=email_try)
            if request.POST['password'] == log_user.password:
                request.session['logged'] = 'yes'
                request.session['name'] = log_user.name
                request.session['alias'] = log_user.alias
                request.session['user_id'] = log_user.id
                print 'login success'
                return redirect('/success')
            else:
                print 'login info mismatch'
                return redirect('/')
        if request.POST['hidden'] == 'add_book':
            book_title = request.POST['title']
            book_author = request.POST['author_list']
            book_review = request.POST['review']
            book_rating = request.POST['rating']
            current_reviewer = User.objects.get(id=request.session['user_id'])
            print 'trying to create author'
            Author.objects.create(
                author_name=book_author
                )   
            print 'author created'
            print 'trying to create book'
            Book.objects.create(
                title=book_title, author = Author.objects.last()
            )
            print 'book created'
            print 'trying to create review'
            Review.objects.create(
                review = book_review, 
                rating=book_rating,
                book=Book.objects.last(),
                reviewer = current_reviewer
            )
            print 'review created'
            return redirect('/success')
        if request.POST['hidden'] == 'separate_review':
            pass
            #flesh out

        else:
            print 'no login tried'
            return redirect('/')

def add(request):
    print 'add view'
    return render(request, 'add.html')

def show_add(request):
    print 'show_add view'
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    user_list = User.objects.all()
    reviews_list = Review.objects.all()
    context = {
        'book_list': book_list,
        'author_list': author_list,
        'user_list': user_list,
        'reviews_list': reviews_list
    }
    return render(request, 'show_add.html', context)

def test(request):
    print 'show_add view'
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    user_list = User.objects.all()
    reviews_list = Review.objects.all()
    context = {
        'book_list': book_list,
        'author_list': author_list,
        'user_list': user_list,
        'reviews_list': reviews_list
    }
    return render(request, 'show_add.html', context)


def success(request):
    print 'success view'
    return render(request, 'success.html')

def user_activity(request):
    print 'user activity view'
    curr_user = User.objects.get(id=request.session['user_id'])
    book_set = curr_user.books.all()
    activity = book_set
    context = {
        'activity': activity 
    }
    return render(reqeust, 'user_activity.html', context)