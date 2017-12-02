# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
# from django.urls import reverse

# Create your views here.
def index(request):
    print 'indesx view'
    return HttpResponse('Hello, world.  You are at the polls index.')

def index2(request):
    latest_question_list = Question.objects.order_by('_pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'lastest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    other_question_pull = Question.objects.get(id=1) #doesnt work for some reason
    context = {
        'q1': other_question_pull
    }
    return render(request, 'polls/detail.html', {'question': question})
    # return render(request, 'polls/detail.html', context)
    #Question equals an object...same as Question.objects.get(id=question_id)

def results(request, question_id):
    response = "You're looking at the results of question {}.".format(question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # works with the replacement of question_id and .format

def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))
#Initially used but replaced by below


def vote2(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 
            'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return Redirect('results', args=(question.id,))
