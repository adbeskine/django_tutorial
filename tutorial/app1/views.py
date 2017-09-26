# from django.shortcuts import render <- what's this?

from django.http import HttpResponse

def index(request):
	return HttpResponse("You are in app1's index, let's learn Django!")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

# Create your views here.
