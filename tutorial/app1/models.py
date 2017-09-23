from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') 

	def __str__(self):
		return 'question: ' + self.question_text + ' date: ' + str(self.pub_date) 

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return 'question: ' + self.question + '/n choice text: ' + self.choice_text + '/n votes: ' + self.votes
# Create your models here.
