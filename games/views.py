from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GamePhrase, Topic
import random
from .forms import AnagramForm

# Create your views here.
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
    for phrase in phrases:
        phrase_list.append(phrase['phrase'].strip().lower())

    return phrase_list

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


'''@login_required
def start_hangman(request):
    if request.method == 'GET':
        word = get_word(request)
        


@login_required
def button(request):
    game_id = int(request.POST['game_id'])

    game = Game.objects.get(game_id=game_id)

    if game.user != request.user:
        return render(request, "hangman.html")
    answer = game.answer

    cur_guess = request.POST['letter']
    guessed = list(game.guessed)

    if game.status == "win" or game.status == "lose":
        generate_finished_game(game)
        return render(request, "hangman.html", {'guessed': guessed, 'game': game})
    if cur_guess not in guessed:
        guessed.append(cur_guess)
        game.guessed = "".join(guessed)
        game.save()
    word_to_display = ""

    match_num = 0
    for char in answer:
        if char in guessed:
            match_num += 1
            word_to_display += char + ' '
        else:
            word_to_display += '_ '

    if match_num == len(answer):
        game.status = "win"
        game.save()
    game.display = word_to_display

    num_wrong_guess = 0
    for char in guessed:
        if char not in answer:
            num_wrong_guess += 1
    if num_wrong_guess >= 10:
        game.status = 'lose'
        game.save()
        num_wrong_guess = 10
    game.image = "/static/images/hang" + str(num_wrong_guess) + ".gif"

    return render(request, "hangman.html", {'guessed': guessed, 'game': game})


def generate_finished_game(game):
    answer = game.answer
    guessed = list(game.guessed)
    if game.status == "win":
        game.display = " ".join(list(answer))
        game.image = "/static/images/hang" + str(wrong_num(guessed, answer)) + ".gif"
        return
    else:
        game.display = word_to_display(guessed, answer)
        game.image = "/static/images/hang10.gif"
        return'''