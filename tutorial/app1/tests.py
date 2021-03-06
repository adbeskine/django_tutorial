import datetime
from django.test import TestCase
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import Question

#-----HELPER METHODS-----#-

def create_question(question_text, days):
	time=timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

	def test_was_published_recently_future_question(self):
		# was_published_recently() returns False for questions published in the future
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_old_question(self):
		# was_published_recently() returns False for questions whose pub_date is older than 1 day
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_recent_question(self):
		# was_published_recently() returns True for questions whose pub_date is withing the last day
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)






class QuestionIndexViewTests(TestCase):
	def test_no_question(self):
		# if no questions exist an appropriate message is displayed
		response = self.client.get(reverse('app1:genericIndex'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_past_question(self):
		# questions with a pub_date in the past are displayed on the index page
		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('app1:genericIndex'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'], ['<Question: Past question.>']
			)

	def test_future_question(self):
		# questions with a pub_date set in the future are NOT displayed on the index page
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('app1:genericIndex'))
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_future_question_and_past_question(self):
		 # when past and future questions exist, only past questions are displayed

		 create_question(question_text="Past question.", days=-30)
		 create_question(question_text="Future question.", days=30)
		 response = self.client.get(reverse('app1:genericIndex'))
		 self.assertQuerysetEqual(
		 	response.context['latest_question_list'], ['<Question: Past question.>'])

	def test_two_past_questions(self):
		# the questions index page may display multiple questions

		create_question(question_text="Past question 1.", days=-30)
		create_question(question_text="Past question 2.", days=-5)
		response = self.client.get(reverse('app1:genericIndex'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2.>', '<Question: Past question 1.>'])




# Create your tests here.
