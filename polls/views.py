from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question


def index(request):
	latest_qeustion_list = Question.objects.order_by("-pub_date")[:5]
	context = {'latest_question_list': latest_qeustion_list}
	return HttpResponse(render(request, 'polls/index.html', context))


def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
	response = "You're looking at results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on quetion %s." % question_id)