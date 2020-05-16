from django.shortcuts import render, redirect
from .forms import Signup_Form
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
	if request.method == "POST":
		form = Signup_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = Signup_Form()

	return render(request, 'accounts/signup.html', {'form': form})

@login_required
def myinfo(request):
	return render(request, 'accounts/myinfo.html')