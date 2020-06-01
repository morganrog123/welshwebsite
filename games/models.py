from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.
class Topic(models.Model):
	TOPIC_CHOICES = []
	data = None
	with open('welsh/static/topics.json', 'r') as topics:
		data = json.load(topics)

	for i in range(0,len(data)):
		topic = data[i].get('name')
		TOPIC_CHOICES.append([topic, topic])

	topic = models.CharField(max_length= 50, choices= TOPIC_CHOICES)

	def __str__(self):
		return self.topic

class GamePhrase(models.Model):
	phrase_topic = models.ForeignKey(Topic, on_delete= models.CASCADE, default= "")
	phrase = models.CharField(max_length= 50, default= "")
	translated_phrase = models.CharField(max_length = 50, default= "")

	def __str__(self):
		return self.phrase

class Hangman(models.Model):
    user = models.ForeignKey(User, default=None, on_delete= models.CASCADE)
    game_id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=20)
    guessed = models.CharField(max_length=27, default="")
    status = models.CharField(max_length=10, default="ongoing")