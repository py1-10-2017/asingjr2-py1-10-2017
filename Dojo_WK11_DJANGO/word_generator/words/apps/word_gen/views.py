# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.crypto
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    string1 = django.utils.crypto.get_random_string(length=14)
    context = {
        'string1': string1
    }
    return render(request, 'word_gen/index.html', context)

def clear(request):
    # print 'counter is ', request.session['counter']
    # del request.session['counter']
    # print 'counter is ', request.session
    print request.session['counter']
    del request.session['counter']
    return redirect('/')
    return redirect('/test')

