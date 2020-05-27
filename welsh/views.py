from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Test
from .forms import TestForm
from django.urls import path
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
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

@login_required
def selectview(request):
	return render(request, 'welsh/select.html')

@login_required
def testview(request):
	urlpath = ''
	if 'year7/topic1' in request.path:
		urlpath = 'year7/topic1'
		tests = Test.objects.filter(test_name= "Fi fy Hunan")
	elif 'year7/topic2' in request.path:
		urlpath = 'year7/topic2'
		tests = Test.objects.filter(test_name= "Gwyliau")
	elif 'year7/topic3' in request.path:
		urlpath = 'year7/topic3'
		tests = Test.objects.filter(test_name= "Ysgol")
	elif 'year7/topic4' in request.path:
		urlpath = 'year7/topic4'
		tests = Test.objects.filter(test_name= "Tywydd")
	elif 'year7/topic5' in request.path:
		urlpath = 'year7/topic5'
		tests = Test.objects.filter(test_name= "Amser")
	elif 'year7/topic6' in request.path:
		urlpath = 'year7/topic6'
		tests = Test.objects.filter(test_name= "Bwyd")
	elif 'year8/topic1' in request.path:
		urlpath = 'year8/topic1'
		tests = Test.objects.filter(test_name= "Ffasiwn")
	elif 'year8/topic2' in request.path:
		urlpath = 'year8/topic2'
		tests = Test.objects.filter(test_name= "Teulu a Ffrindiau")
	elif 'year8/topic3' in request.path:
		urlpath = 'year8/topic3'
		tests = Test.objects.filter(test_name= "Trefn Ddyddiol")
	elif 'year8/topic4' in request.path:
		urlpath = 'year8/topic4'
		tests = Test.objects.filter(test_name= "Anifeiliad Anwes")
	elif 'year8/topic5' in request.path:
		urlpath = 'year8/topic5'
		tests = Test.objects.filter(test_name= "Cartref")
	elif 'year9/topic1' in request.path:
		urlpath = 'year9/topic1'
		tests = Test.objects.filter(test_name= "Cysyllteiriau ac Idiomau")
	elif 'year9/topic2' in request.path:
		urlpath = 'year9/topic2'
		tests = Test.objects.filter(test_name= "Hamdden a Hobiau")
	elif 'year9/topic3' in request.path:
		urlpath = 'year9/topic3'
		tests = Test.objects.filter(test_name= "Chwaraeon")
	elif 'year9/topic4' in request.path:
		urlpath = 'year9/topic4'
		tests = Test.objects.filter(test_name= "Digwyddiadau Arbennig")
	elif 'year9/topic5' in request.path:
		urlpath = 'year9/topic5'
		tests = Test.objects.filter(test_name= "Amser Gorffenol")
	elif 'year10/topic1' in request.path:
		urlpath = 'year10/topic1'
		tests = Test.objects.filter(test_name= "Cerddoriaeth")
	elif 'year10/topic2' in request.path:
		urlpath = 'year10/topic2'
		tests = Test.objects.filter(test_name= "Cymru, Digwylliant ac Enwogion")
	elif 'year10/topic3' in request.path:
		urlpath = 'year10/topic3'
		tests = Test.objects.filter(test_name= "Cadw'n Iach")
	elif 'year10/topic4' in request.path:
		urlpath = 'year10/topic4'
		tests = Test.objects.filter(test_name= "Y Penwythnos")
	elif 'year10/topic5' in request.path:
		urlpath = 'year10/topic5'
		tests = Test.objects.filter(test_name= "Amser Dyfodol")
	elif 'year11/topic1' in request.path:
		urlpath = 'year11/topic1'
		tests = Test.objects.filter(test_name= "Gwaith")
	elif 'year11/topic2' in request.path:
		urlpath = 'year11/topic2'
		tests = Test.objects.filter(test_name= "Problemau Pobl Ifanc")
	elif 'year11/topic3' in request.path:
		urlpath = 'year11/topic3'
		tests = Test.objects.filter(test_name= "Y Amgylchedd")
	elif 'year11/topic4' in request.path:
		urlpath = 'year11/topic4'
		tests = Test.objects.filter(test_name= "Cyfryngau")
	elif 'year11/topic5' in request.path:
		urlpath = 'year11/topic5'
		tests = Test.objects.filter(test_name= "Technoleg")
	else:
		raise Http404()
	# function needed later to get tests
	context = {
		"tests": tests,
		"urlpath": urlpath
	}
	return render(request, 'welsh/test.html', context)

@login_required
def checkresults(request):
	urlpath = ''
	if 'year7/topic1' in request.path:
		urlpath = 'year7/topic1'
		answers = Test.objects.filter(test_name= "Fi fy Hunan").values()
	elif 'year7/topic2' in request.path:
		urlpath = 'year7/topic2'
		answers = Test.objects.filter(test_name= "Gwyliau").values()
	elif 'year7/topic3' in request.path:
		urlpath = 'year7/topic3'
		answers = Test.objects.filter(test_name= "Ysgol").values()
	elif 'year7/topic4' in request.path:
		urlpath = 'year7/topic4'
		answers = Test.objects.filter(test_name= "Tywydd").values()
	elif 'year7/topic5' in request.path:
		urlpath = 'year7/topic5'
		answers = Test.objects.filter(test_name= "Amser").values()
	elif 'year7/topic6' in request.path:
		urlpath = 'year7/topic6'
		answers = Test.objects.filter(test_name= "Bwyd").values()
	elif 'year8/topic1' in request.path:
		urlpath = 'year8/topic1'
		answers = Test.objects.filter(test_name= "Ffasiwn").values()
	elif 'year8/topic2' in request.path:
		urlpath = 'year8/topic2'
		answers = Test.objects.filter(test_name= "Teulu a Ffrindiau").values()
	elif 'year8/topic3' in request.path:
		urlpath = 'year8/topic3'
		answers = Test.objects.filter(test_name= "Trefn Ddyddiol").values()
	elif 'year8/topic4' in request.path:
		urlpath = 'year8/topic4'
		answers = Test.objects.filter(test_name= "Anifeiliad Anwes").values()
	elif 'year8/topic5' in request.path:
		urlpath = 'year8/topic5'
		answers = Test.objects.filter(test_name= "Cartref").values()
	elif 'year9/topic1' in request.path:
		urlpath = 'year9/topic1'
		answers = Test.objects.filter(test_name= "Cysyllteiriau ac Idiomau").values()
	elif 'year9/topic2' in request.path:
		urlpath = 'year9/topic2'
		answers = Test.objects.filter(test_name= "Hamdden a Hobiau").values()
	elif 'year9/topic3' in request.path:
		urlpath = 'year9/topic3'
		answers = Test.objects.filter(test_name= "Chwaraeon").values()
	elif 'year9/topic4' in request.path:
		urlpath = 'year9/topic4'
		answers = Test.objects.filter(test_name= "Digwyddiadau Arbennig").values()
	elif 'year9/topic5' in request.path:
		urlpath = 'year9/topic5'
		answers = Test.objects.filter(test_name= "Amser Gorffenol").values()
	elif 'year10/topic1' in request.path:
		urlpath = 'year10/topic1'
		answers = Test.objects.filter(test_name= "Cerddoriaeth").values()
	elif 'year10/topic2' in request.path:
		urlpath = 'year10/topic2'
		answers = Test.objects.filter(test_name= "Cymru, Digwylliant ac Enwogion").values()
	elif 'year10/topic3' in request.path:
		urlpath = 'year10/topic3'
		answers = Test.objects.filter(test_name= "Cadw'n Iach").values()
	elif 'year10/topic4' in request.path:
		urlpath = 'year10/topic4'
		answers = Test.objects.filter(test_name= "Y Penwythnos").values()
	elif 'year10/topic5' in request.path:
		urlpath = 'year10/topic5'
		answers = Test.objects.filter(test_name= "Amser Dyfodol").values()
	elif 'year11/topic1' in request.path:
		urlpath = 'year11/topic1'
		answers = Test.objects.filter(test_name= "Gwaith").values()
	elif 'year11/topic2' in request.path:
		urlpath = 'year11/topic2'
		answers = Test.objects.filter(test_name= "Problemau Pobl Ifanc").values()
	elif 'year11/topic3' in request.path:
		urlpath = 'year11/topic3'
		answers = Test.objects.filter(test_name= "Y Amgylchedd").values()
	elif 'year11/topic4' in request.path:
		urlpath = 'year11/topic4'
		answers = Test.objects.filter(test_name= "Cyfryngau").values()
	elif 'year11/topic5' in request.path:
		urlpath = 'year11/topic5'
		answers = Test.objects.filter(test_name= "Technoleg").values()
	else:
		raise Http404()
	# function needed later to get tests

	if request.method == "POST":
		form = TestForm(request.POST)
		score = 0
		answer_values = []
		for answer in answers:
			answer_values.append(answer['answer_1'])
			answer_values.append(answer['answer_2'])
			answer_values.append(answer['answer_3'])
			answer_values.append(answer['answer_4'])
			answer_values.append(answer['answer_5'])
			answer_values.append(answer['answer_6'])
			answer_values.append(answer['answer_7'])
			answer_values.append(answer['answer_8'])
			answer_values.append(answer['answer_9'])
			answer_values.append(answer['answer_10'])

		if form.is_valid() == False:
			return render(request, 'welsh/test.html')
		else:
			if form.cleaned_data['answer_1'] == answer_values[0]:
				score += 1
			if form.cleaned_data['answer_2'] == answer_values[1]:
				score += 1
			if form.cleaned_data['answer_3'] == answer_values[2]:
				score += 1
			if form.cleaned_data['answer_4'] == answer_values[3]:
				score += 1
			if form.cleaned_data['answer_5'] == answer_values[4]:
				score += 1
			if form.cleaned_data['answer_6'] == answer_values[5]:
				score += 1
			if form.cleaned_data['answer_7'] == answer_values[6]:
				score += 1
			if form.cleaned_data['answer_8'] == answer_values[7]:
				score += 1
			if form.cleaned_data['answer_9'] == answer_values[8]:
				score += 1
			if form.cleaned_data['answer_10'] == answer_values[9]:
				score += 1
			
			context = {
					'score': score,
					'form': form,
					'answer_values': answer_values,
					'urlpath': urlpath
					}
		
		return render(request, 'welsh/result.html', context)

	else:
		return render(request, 'welsh/test.html', form(request))