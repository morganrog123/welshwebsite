from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Signup_Form(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class Edit_Info_Form(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ('username', 'email')