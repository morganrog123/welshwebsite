from django.shortcuts import render, redirect
from .forms import Signup_Form, Edit_Info_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def signup(request):
	if request.user.is_authenticated == True:
		return redirect('home')
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

@login_required
def editinfo(request):
	if request.method == "POST":
		edit_form = Edit_Info_Form(request.POST, instance= request.user)

		if edit_form.is_valid():
			edit_form.save()
			return redirect('myinfo')
	else:
		edit_form = Edit_Info_Form(instance= request.user)
		return render(request, 'accounts/editinfo.html', {'form': edit_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password has been updated!')
            return redirect('myinfo')
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepassword.html', {'form': password_form})