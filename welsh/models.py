from django.db import models

# Create your models here.
class Phrase(models.Model):
	welsh_text = models.CharField(max_length=100)
	english_text = models.CharField(max_length=100)

	def __str__(self):
		return self.word_text
