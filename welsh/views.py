from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Test, LessonPhrase, LessonStart
from .forms import TestForm, LessonForm
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
		tests = Test.objects.filter(test_name= "Ardal")
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
		answers = Test.objects.filter(test_name= "Ardal").values()
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

		if form.is_valid():
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
		return render(request, 'welsh/test.html', {'form': form})

@login_required
def getlessonphrases(request):
	urlpath = ''
	if 'year7/topic1/lesson/1' in request.path:
		urlpath = 'year7/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Fi fy Hunan", lesson_no= 1).values()
	elif 'year7/topic1/lesson/2' in request.path:
		urlpath = 'year7/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Fi fy Hunan", lesson_no= 2).values()
	elif 'year7/topic2/lesson/1' in request.path:
		urlpath = 'year7/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Gwyliau", lesson_no= 1).values()
	elif 'year7/topic2/lesson/2' in request.path:
		urlpath = 'year7/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Gwyliau", lesson_no= 2).values()
	elif 'year7/topic2/lesson/3' in request.path:
		urlpath = 'year7/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Gwyliau", lesson_no= 3).values()
	elif 'year7/topic3/lesson/1' in request.path:
		urlpath = 'year7/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Ysgol", lesson_no= 1).values()
	elif 'year7/topic3/lesson/2' in request.path:
		urlpath = 'year7/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Ysgol", lesson_no= 2).values()
	elif 'year7/topic4/lesson/1' in request.path:
		urlpath = 'year7/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Tywydd", lesson_no= 1).values()
	elif 'year7/topic5/lesson/1' in request.path:
		urlpath = 'year7/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Amser", lesson_no= 1).values()
	elif 'year7/topic5/lesson/2' in request.path:
		urlpath = 'year7/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Amser", lesson_no= 2).values()
	elif 'year7/topic6/lesson/1' in request.path:
		urlpath = 'year7/topic6'
		phrases = LessonPhrase.objects.filter(topic= "Bwyd", lesson_no= 1).values()
	elif 'year7/topic6/lesson/2' in request.path:
		urlpath = 'year7/topic6'
		phrases = LessonPhrase.objects.filter(topic= "Bwyd", lesson_no= 2).values()
	elif 'year8/topic1/lesson/1' in request.path:
		urlpath = 'year8/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Ffasiwn", lesson_no= 1).values()
	elif 'year8/topic1/lesson/2' in request.path:
		urlpath = 'year8/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Ffasiwn", lesson_no= 2).values()
	elif 'year8/topic1/lesson/3' in request.path:
		urlpath = 'year8/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Ffasiwn", lesson_no= 3).values()
	elif 'year8/topic2/lesson/1' in request.path:
		urlpath = 'year8/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Teulu a Ffrindiau", lesson_no= 1).values()
	elif 'year8/topic2/lesson/2' in request.path:
		urlpath = 'year8/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Teulu a Ffrindiau", lesson_no= 2).values()
	elif 'year8/topic3/lesson/1' in request.path:
		urlpath = 'year8/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Trefn Ddyddiol", lesson_no= 1).values()
	elif 'year8/topic4/lesson/1' in request.path:
		urlpath = 'year8/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Anifeiliad Anwes", lesson_no= 1).values()
	elif 'year8/topic5/lesson/1' in request.path:
		urlpath = 'year8/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Cartref", lesson_no= 1).values()
	elif 'year9/topic1/lesson/1' in request.path:
		urlpath = 'year9/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Ardal", lesson_no = 1).values()
	elif 'year9/topic2/lesson/1' in request.path:
		urlpath = 'year9/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Hamdden a Hobiau", lesson_no= 1).values()
	elif 'year9/topic3/lesson/1' in request.path:
		urlpath = 'year9/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Chwaraeon", lesson_no= 1).values()
	elif 'year9/topic4/lesson/1' in request.path:
		urlpath = 'year9/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Digwyddiadau Arbennig", lesson_no= 1).values()
	elif 'year9/topic5/lesson/1' in request.path:
		urlpath = 'year9/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Amser Gorffenol", lesson_no= 1).values()
	elif 'year9/topic5/lesson/2' in request.path:
		urlpath = 'year9/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Amser Gorffenol", lesson_no= 2).values()
	elif 'year10/topic1/lesson/1' in request.path:
		urlpath = 'year10/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Cerddoriaeth", lesson_no= 1).values()
	elif 'year10/topic2/lesson/1' in request.path:
		urlpath = 'year10/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Cymru, Digwylliant ac Enwogion", lesson_no= 1).values()
	elif 'year10/topic2/lesson/2' in request.path:
		urlpath = 'year10/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Cymru, Digwylliant ac Enwogion", lesson_no= 2).values()
	elif 'year10/topic2/lesson/3' in request.path:
		urlpath = 'year10/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Cymru, Digwylliant ac Enwogion", lesson_no= 3).values()
	elif 'year10/topic3/lesson/1' in request.path:
		urlpath = 'year10/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Cadw'n Iach", lesson_no= 1).values()
	elif 'year10/topic3/lesson/2' in request.path:
		urlpath = 'year10/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Cadw'n Iach", lesson_no= 2).values()
	elif 'year10/topic4/lesson/1' in request.path:
		urlpath = 'year10/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Y Penwythnos", lesson_no= 1).values()
	elif 'year10/topic4/lesson/2' in request.path:
		urlpath = 'year10/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Y Penwythnos", lesson_no= 2).values()
	elif 'year10/topic5/lesson/1' in request.path:
		urlpath = 'year10/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Amser Dyfodol", lesson_no= 1).values()
	elif 'year11/topic1/lesson/1' in request.path:
		urlpath = 'year11/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Gwaith", lesson_no= 1).values()
	elif 'year11/topic1/lesson/2' in request.path:
		urlpath = 'year11/topic1'
		phrases = LessonPhrase.objects.filter(topic= "Gwaith", lesson_no= 2).values()
	elif 'year11/topic2/lesson/1' in request.path:
		urlpath = 'year11/topic2'
		phrases = LessonPhrase.objects.filter(topic= "Problemau Pobl Ifanc", lesson_no= 1).values()
	elif 'year11/topic3/lesson/1' in request.path:
		urlpath = 'year11/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Y Amgylchedd", lesson_no= 1).values()
	elif 'year11/topic3/lesson/2' in request.path:
		urlpath = 'year11/topic3'
		phrases = LessonPhrase.objects.filter(topic= "Y Amgylchedd", lesson_no= 2).values()
	elif 'year11/topic4/lesson/1' in request.path:
		urlpath = 'year11/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Cyfryngau", lesson_no= 1).values()
	elif 'year11/topic4/lesson/2' in request.path:
		urlpath = 'year11/topic4'
		phrases = LessonPhrase.objects.filter(topic= "Cyfryngau", lesson_no= 2).values()
	elif 'year11/topic5/lesson/1' in request.path:
		urlpath = 'year11/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Technoleg", lesson_no= 1).values()
	elif 'year11/topic5/lesson/2' in request.path:
		urlpath = 'year11/topic5'
		phrases = LessonPhrase.objects.filter(topic= "Technoleg", lesson_no= 2).values()

	request.session['urlpath'] = urlpath
	return phrases

@login_required
def lessonview(request):
	if request.method == "GET":
		phrases = getlessonphrases(request)
		urlpath = request.session['urlpath']
		phrase_list = []
		status = "learning"

		for phrase in phrases:
			phrase_list.append(phrase)

		lesson = LessonStart(user=request.user, current_phrase=phrase_list[0].get('phrase'), current_translated_phrase=phrase_list[0].get('translated_phrase'), count = 0)
		lesson.save()

		context = {
			'urlpath': urlpath,
			'lesson': lesson,
			'phrase_list': phrase_list,
			'status': status
		}

		return render(request, 'welsh/lesson.html', context)
	else:
		return button(request)

@login_required
def button(request):
	phrases = getlessonphrases(request)
	urlpath = request.session['urlpath']
	lesson_id = int(request.POST['lesson_id'])
	lesson = LessonStart.objects.get(lesson_id= lesson_id)
	phrase_list = []
	current_phrase = lesson.current_phrase
	current_translated_phrase = lesson.current_translated_phrase
	count = lesson.count
	context = {'urlpath': urlpath,'lesson': lesson}


	for phrase in phrases:
		phrase_list.append(phrase)

	if "nextbtn" in request.POST:
		lesson.status = "input"
		lesson.save()
		context = {
			'urlpath': urlpath,
			'lesson': lesson,
		}
		return render(request, 'welsh/lesson.html', context)

	form = LessonForm(request.POST)
	if "guess" in request.POST:
		lesson.status = "check"
		lesson.save()
		context = {
			'urlpath': urlpath,
			'lesson': lesson,
			'form': form
		}
		return render(request, 'welsh/lesson.html', context)

	if "next_phrase" in request.POST:
		lesson.count += 1
		lesson.status = "learning"
		lesson.save()

	if lesson.count >= len(phrase_list):
		lesson.status = "finished"
		lessonfinish(request)
		lesson.save()
	else:
		lesson.current_phrase = phrase_list[lesson.count].get('phrase')
		lesson.current_translated_phrase = phrase_list[lesson.count].get('translated_phrase')
		lesson.save()

	if lesson.status == "learning":
		context = {
			'urlpath': urlpath,
			'lesson': lesson,
		}

	return render(request, 'welsh/lesson.html', context)

def lessonfinish(request):
	urlpath = request.session['urlpath']
	lesson_id = int(request.POST['lesson_id'])
	lesson = LessonStart.objects.get(lesson_id= lesson_id)
	return render(request, 'welsh/lesson.html', {'urlpath': urlpath, 'lesson': lesson})