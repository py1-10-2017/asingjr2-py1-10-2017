# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import 

# Create your views here.
def index(request):
    print 'indesx view'
    return HttpResponse('Hello, world.  You are not at the polls index.')

def index2(request):
    latest_question_list = Question.objects.order_by('_pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("'You're looking at question {}'.format(question_id)")
#check to see if this works with .format

def results(request, question_id):
    response = "You're looking at the results of question {}.".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("'You're voting on question {}.'.format(question_id)")


