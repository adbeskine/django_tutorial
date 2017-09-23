# from django.shortcuts import render <- what's this?

from django.http import HttpResponse

def index(request):
	return HttpResponse("You are in app1's index, let's learn Django!")

# Create your views here.
