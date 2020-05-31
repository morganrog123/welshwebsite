from django import forms
from .models import Test

class TestForm(forms.Form):
	answer_1 = forms.CharField(max_length= 50, required= False)
	answer_2 = forms.CharField(max_length= 50, required= False)
	answer_3 = forms.CharField(max_length= 50, required= False)
	answer_4 = forms.CharField(max_length= 50, required= False)
	answer_5 = forms.CharField(max_length= 50, required= False)
	answer_6 = forms.CharField(max_length= 50, required= False)
	answer_7 = forms.CharField(max_length= 50, required= False)
	answer_8 = forms.CharField(max_length= 50, required= False)
	answer_9 = forms.CharField(max_length= 50, required= False)
	answer_10 = forms.CharField(max_length= 50, required= False)

	class Meta:
		model = Test
		fields = ('answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5', 'answer_6',
			'answer_7', 'answer_8', 'answer_9', 'answer_10')

class LessonForm(forms.Form):
	guess = forms.CharField(max_length= 150)