# from django.shortcuts import render <- what's this?

from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
from django.urls import reverse
from django.utils import timezone

# --------------------------BASIC VIEWS -----------------------------------#

def index(request):
	return HttpResponse("You are in app1's index, let's learn Django!")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)


#----------------------------FUNCTIONAL VIEWS------------------------------#

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

def detail_with_404(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'app1/detail.html', {'question': question})

#----------------------------------SHORTCUTS-----------------------------------------#

# 1. define variables
# 2. pass it into context format (note you can skip this and put a dictionary directly into the render method in step 3)
# 3. render(request, template, context)
def index_html_shorthand(request):
	latest_question_list=Question.objects.order_by('pub_date')[:5]
	context = {'latest_question_list' : latest_question_list,}
	return render(request, 'app1/index.html', context)

def detail_404_shortcut(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'app1/detail.html', {'question': question})


#---------------------------------------OTHER-------------------------------------#

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'app1/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		# redisplay the question voting form
		return render(request, 'app1/detail.html', {
			'question': question,
			'error_mesage': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('app1:results', args=(question.id,)))

#---------------------------------------------------------------------------------------#

#------------------------------GENERIC VIEWS -------------------------------------------#

from django.views import generic

class IndexView(generic.ListView):
	template_name = 'app1/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions excluding those published in the future."""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'app1/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'app1/results.html'


# Create your views here.
