from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""class GamePhrase(models.Model):
	TOPIC_CHOICES = (
		('FH',  'Fi fy Hunan'), ('Gw', 'Gwyliau'), ('Ys' 'Ysgol'), ('Ty', 'Tywydd'), ('Am', 'Amser'), ('Bw', 'Bwyd'),
		('Ff', 'Ffasiwn'), ('TF', 'Teulu a Ffrindiau'), ('TD', 'Trefn Ddyddiol'), ('AA', 'Anifeiliad Anwes'), ('Ca', 'Cartref'),
		('CI', 'Cysyllteiriau ac Idiomau'), ('HH', 'Hamdden a Hobiau'), ('Ch', 'Chwaraeon'), ('DA', 'Digwyddiadau Arbennig'), ('AG', 'Amser Gorffenol'),
		('Ce', 'Cerddioraeth'), ('CDE', 'Cymru, Digwylliant ac Enwogion'), ('CaI', "Cadw'n Iach"), ('YP', 'Y Penwythnos'), ('AD', 'Amser Dyfodol'),
		('Gw', 'Gwaith'), ('PPI', 'Problemau Pobl Ifanc'), ('YA', 'Y Amgylchedd'), ('Cy', 'Cyfryngau'), ('Te', 'Technoleg'),
		)
	
	welsh_text = models.CharField(max_length= 20)
	english_text = models.CharField(max_length= 20)
	topic = models.CharField(max_length = 20, choices= TOPIC_CHOICES)

	def __str__(self):
		return self.welsh_text

class Hangman(models.Model):
	user = models.ForeignKey(User, default= None)
	game_id = models.AutoField(primary_key= True)
	answer = models.CharField(max_length= 20)
	guessed = models.CharField(max_length= 10, default= "")
	status = models.CharField(max_length= 10, default= "ongoing")"""