from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GamePhrase, Topic, Hangman
import random
from .forms import AnagramForm, QuickfireForm
from datetime import datetime

# Create your views here.
@login_required
def gameselect(request):
    return render(request, 'games/game_select.html')

def getPhrases(request):
    urlpath = ''
    if 'year7/topic1' in request.path:
        urlpath = 'year7/topic1'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Fi fy Hunan").values()
    elif 'year7/topic2' in request.path:
        urlpath = 'year7/topic2'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Gwyliau").values()
    elif 'year7/topic3' in request.path:
        urlpath = 'year7/topic3'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Ysgol").values()
    elif 'year7/topic4' in request.path:
        urlpath = 'year7/topic4'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Tywydd").values()
    elif 'year7/topic5' in request.path:
        urlpath = 'year7/topic5'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Amser").values()
    elif 'year7/topic6' in request.path:
        urlpath = 'year7/topic6'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Bwyd").values()
    elif 'year8/topic1' in request.path:
        urlpath = 'year8/topic1'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Ffasiwn").values()
    elif 'year8/topic2' in request.path:
        urlpath = 'year8/topic2'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Teulu a Ffrindiau").values()
    elif 'year8/topic3' in request.path:
        urlpath = 'year8/topic3'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Trefn Ddyddiol").values()
    elif 'year8/topic4' in request.path:
        urlpath = 'year8/topic4'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Anifeiliad Anwes").values()
    elif 'year8/topic5' in request.path:
        urlpath = 'year8/topic5'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Cartref").values()
    elif 'year9/topic1' in request.path:
        urlpath = 'year9/topic1'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Cysyllteiriau ac Idiomau").values()
    elif 'year9/topic2' in request.path:
        urlpath = 'year9/topic2'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Hamdden a Hobiau").values()
    elif 'year9/topic3' in request.path:
        urlpath = 'year9/topic3'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Chwaraeon").values()
    elif 'year9/topic4' in request.path:
        urlpath = 'year9/topic4'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Digwyddiadau Arbennig").values()
    elif 'year9/topic5' in request.path:
        urlpath = 'year9/topic5'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Amser Gorffenol").values()
    elif 'year10/topic1' in request.path:
        urlpath = 'year10/topic1'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Cerddoriaeth").values()
    elif 'year10/topic2' in request.path:
        urlpath = 'year10/topic2'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Cymru, Digwylliant ac Enwogion").values()
    elif 'year10/topic3' in request.path:
        urlpath = 'year10/topic3'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Cadw'n Iach").values()
    elif 'year10/topic4' in request.path:
        urlpath = 'year10/topic4'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Y Penwythnos").values()
    elif 'year10/topic5' in request.path:
        urlpath = 'year10/topic5'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Amser Dyfodol").values()
    elif 'year11/topic1' in request.path:
        urlpath = 'year11/topic1'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Gwaith").values()
    elif 'year11/topic2' in request.path:
        urlpath = 'year11/topic2'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Problemau Pobl Ifanc").values()
    elif 'year11/topic3' in request.path:
        urlpath = 'year11/topic3'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Y Amgylchedd").values()
    elif 'year11/topic4' in request.path:
        urlpath = 'year11/topic4'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Cyfryngau").values()
    elif 'year11/topic5' in request.path:
        urlpath = 'year11/topic5'
        phrases = GamePhrase.objects.filter(phrase_topic__topic__exact= "Technoleg").values()

    request.session['urlpath'] = urlpath
    return phrases

def load_list(request):
    phrases = getPhrases(request)
    phrase_list = []
    translate_list = []

    for phrase in phrases:
        phrase_list.append(phrase['phrase'].strip().lower())
        translate_list.append(phrase['translated_phrase'].strip().lower())

    return phrase_list
    return translate_list

def get_word(request):
    phrase_list = load_list(request)
    if len(phrase_list) == 0:
        return get_word(request)
    else:
        word = random.choice(phrase_list)
    
    return word

@login_required
def start_anagram(request):
    getPhrases(request)
    urlpath = request.session['urlpath']
    word = get_word(request)
    request.session['word'] = word
    word_list = list(word)
    random.shuffle(word_list)
    result = ''.join(word_list)

    context = {
        'result': result,
        'urlpath': urlpath
    }

    return render(request, 'games/anagram.html', context)

@login_required
def anagram_finish(request):
    getPhrases(request)
    urlpath = request.session['urlpath']
    correct_word = request.session['word']

    if request.method == "POST":
        form = AnagramForm(request.POST)
        if form.is_valid():
            context = {
                    'form': form,
                    'correct_word': correct_word,
                    'urlpath': urlpath
                    }

            return render(request, 'games/anagram_result.html', context)
    else:
        return render(request, 'games/anagram.html', {'form': form})


@login_required
def start_quickfire(request):
    request.session['start_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    phrases = getPhrases(request)
    urlpath = request.session['urlpath']
    word = get_word(request)
    request.session['word'] = word
    translated_word = ""
    request.session['translated_phrase'] = translated_word

    for phrase in phrases:
        if phrase['phrase'].strip().lower() == word:
            translated_phrase = phrase['translated_phrase'].strip().lower()
            request.session['translated_phrase'] = translated_phrase

    context = {
        'word': word,
        'urlpath': urlpath
    }

    return render(request, 'games/quickfire.html', context)

@login_required
def quickfire_finish(request):
    urlpath = request.session['urlpath']
    translated_word = request.session['translated_phrase']

    if request.method == "POST":
        form = QuickfireForm(request.POST)
        if form.is_valid():
            start_time = request.session['start_time']
            end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            tdelta = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S') - datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            time_delta = int(tdelta.total_seconds())
            score = (50 - time_delta) * 20
            if time_delta > 49: score = 0
        context = {
                'form': form,
                'translated_word': translated_word,
                'urlpath': urlpath,
                'score': score
                }

        return render(request, 'games/quickfire_result.html', context)
    else:
        return render(request, 'games/quickfire.html', {'form': form})


def get_lives():
    num_lives = 6
    return num_lives

@login_required
def start_hangman(request):
    if request.method == 'GET':
        getPhrases(request)
        urlpath = request.session['urlpath']
        word = get_word(request)
        game = Hangman(user=request.user, answer=word)
        game.save()
        game.display = "_ " * len(word)
        word
        num_lives = get_lives()

        context = {'num_lives': num_lives, 
                    'guessed': [], 
                    "game": game,
                    "urlpath": urlpath
                }

        return render(request, "games/hangman.html", context)
    else:
        return button(request)


@login_required
def button(request):
    getPhrases(request)
    urlpath = request.session['urlpath']
    game_id = int(request.POST['game_id'])
    game = Hangman.objects.get(game_id=game_id)
    answer = game.answer
    guess = request.POST['letter']
    guessed_list = list(game.guessed)
    num_lives = get_lives()

    if game.status == "win" or game.status == "lose":
        hangman_finish(game)
        return render(request, "games/hangman.html", {'urlpath': urlpath, 'guessed': guessed_list, 'game': game})
    if guess not in guessed_list:
        guessed_list.append(guess)
        game.guessed = "".join(guessed_list)
        game.save()

    word_to_display = ""

    matched_num = 0
    for char in answer:
        if char in guessed_list:
            matched_num += 1
            word_to_display += char + ' '
        else:
            word_to_display += '_ '

    if matched_num == len(answer):
        game.status = "win"
        game.save()
    game.display = word_to_display

    for char in guessed_list:
        if char not in answer:
            num_lives -= 1
    if num_lives <= 0:
        game.status = 'lose'
        game.save()

    context = {
        'num_lives': num_lives,
        'guessed': guessed_list,
        'game': game,
        'urlpath': urlpath
    }

    return render(request, "games/hangman.html", context)

@login_required
def hangman_finish(game):
    answer = game.answer
    guessed_list = list(game.guessed)
    if game.status == "win":
        game.display = " ".join(list(answer))
        return
    else:
        game.display = word_to_display(guessed_list, answer)
        return