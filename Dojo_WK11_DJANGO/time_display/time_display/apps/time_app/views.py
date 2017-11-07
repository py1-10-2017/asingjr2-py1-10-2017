# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime 
import time

now = datetime.datetime.now()
# Create your views here.
def index(request):
    context = {
        'now' : now, 
        'detail': now.strftime('%m: %d, %Y "\n"%I:%m %p')
    }
    return render(request, 'time_app/index.html', context)
