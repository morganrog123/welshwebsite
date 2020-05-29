from django import forms

class AnagramForm(forms.Form):
	guess = forms.CharField(max_length= 100)

class QuickfireForm(forms.Form):
	guess = forms.CharField(max_length= 100)