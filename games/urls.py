# URL path configuration
from django.urls import path
from . import views


urlpatterns = [
    path('year7/topic1/game/anagram/', views.start_quickfire, name= 'anagram'),
    path('year7/topic1/game/anagram_result/', views.quickfire_finish, name= 'anagram_result')
]