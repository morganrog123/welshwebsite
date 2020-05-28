# URL path configuration
from django.urls import path
from . import views


urlpatterns = [
    path('year7/topic1/game/anagram/', views.start_anagram, name= 'anagram'),
    path('year7/topic1/game/anagram_result/', views.anagram_finish, name= 'anagram_result')
]