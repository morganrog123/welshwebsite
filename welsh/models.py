from django.db import models
import json
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):

	TOPIC_CHOICES = []
	data = None
	with open('welsh/static/topics.json', 'r') as topics:
		data = json.load(topics)

	for i in range(0,len(data)):
		topic = data[i].get('name')
		TOPIC_CHOICES.append([topic, topic])

	test_name = models.CharField(max_length= 50, choices= TOPIC_CHOICES)
	question_1 = models.CharField(max_length= 100, default="")
	answer_1 = models.CharField(max_length= 100, default= "")
	question_2 = models.CharField(max_length= 100, default="")
	answer_2 = models.CharField(max_length= 100, default= "")
	question_3 = models.CharField(max_length= 100, default="")
	answer_3 = models.CharField(max_length= 100, default= "")
	question_4 = models.CharField(max_length= 100, default="")
	answer_4 = models.CharField(max_length= 100, default= "")
	question_5 = models.CharField(max_length= 100, default="")
	answer_5 = models.CharField(max_length= 100, default= "")
	question_6 = models.CharField(max_length= 100, default="")
	answer_6 = models.CharField(max_length= 100, default= "")
	question_7 = models.CharField(max_length= 100, default="")
	answer_7 = models.CharField(max_length= 100, default= "")
	question_8 = models.CharField(max_length= 100, default="")
	answer_8 = models.CharField(max_length= 100, default= "")
	question_9 = models.CharField(max_length= 100, default="")
	answer_9 = models.CharField(max_length= 100, default= "")
	question_10 = models.CharField(max_length= 100, default="")
	answer_10 = models.CharField(max_length= 100, default= "")

	def __str__(self):
		return self.test_name