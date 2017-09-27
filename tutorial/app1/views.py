# from django.shortcuts import render <- what's this?

from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render

def index(request):
	return HttpResponse("You are in app1's index, let's learn Django!")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response="You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	response="you're voting on question %s."
	return HttpResponse(response % question_id)

def index_generated_variables(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	output = ' '.join([q.question_text + '|||' for q in latest_question_list])
	return HttpResponse(output)


# 1. get the template
# 2. define any variables used in the template (context)
# 3. normal httpresponse with render method
def index_html_longhand(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	template = loader.get_template('app1/index.html')
	context={
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))


def index_html_shorthand(request):
	latest_question_list=Question.objects.order_by('pub_date')[:5]
	context = {'latest_question_list' : latest_question_list,}
	return render(request, 'app1/index.html', context)

# Create your views here.
