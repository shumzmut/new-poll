import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('Date published')

	def __str__(self): # __unicode__ on Python 2 
		return self.question_text

	# def was_published_recently(self):
	# 	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def was_published_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now	
	#Returns true if publishing date 'pub_date' is before now AND greater than or equal to 1 day ago

class Choice(models.Model):
	question=models.ForeignKey(Question)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text