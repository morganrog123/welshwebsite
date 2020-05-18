from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'welsh/index.html')

@login_required
def home(request):
	return render(request, 'welsh/home.html')

# View for each year the user selects
@login_required
def year7(request):
	return render(request, 'welsh/year7.html')

@login_required
def year8(request):
	return render(request, 'welsh/year8.html')

@login_required
def year9(request):
	return render(request, 'welsh/year9.html')

@login_required
def year10(request):
	return render(request, 'welsh/year10.html')

@login_required
def year11(request):
	return render(request, 'welsh/year11.html')