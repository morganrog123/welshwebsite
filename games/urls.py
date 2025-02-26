# URL path configuration
from django.urls import path, include
from . import views

quickfireresultpatterns = [
	path('year7/topic1/games/quickfire/result/', views.quickfire_finish, name='y7_t1_quickfire_result'),
	path('year7/topic2/games/quickfire/result/', views.quickfire_finish, name='y7_t2_quickfire_result'),
	path('year7/topic3/games/quickfire/result/', views.quickfire_finish, name='y7_t3_quickfire_result'),
	path('year7/topic4/games/quickfire/result/', views.quickfire_finish, name='y7_t4_quickfire_result'),
	path('year7/topic5/games/quickfire/result/', views.quickfire_finish, name='y7_t5_quickfire_result'),
	path('year7/topic6/games/quickfire/result/', views.quickfire_finish, name='y7_t6_quickfire_result'),
	path('year8/topic1/games/quickfire/result/', views.quickfire_finish, name='y8_t1_quickfire_result'),
	path('year8/topic2/games/quickfire/result/', views.quickfire_finish, name='y8_t2_quickfire_result'),
	path('year8/topic3/games/quickfire/result/', views.quickfire_finish, name='y8_t3_quickfire_result'),
	path('year8/topic4/games/quickfire/result/', views.quickfire_finish, name='y8_t4_quickfire_result'),
	path('year8/topic5/games/quickfire/result/', views.quickfire_finish, name='y8_t5_quickfire_result'),
	path('year9/topic1/games/quickfire/result/', views.quickfire_finish, name='y9_t1_quickfire_result'),
	path('year9/topic2/games/quickfire/result/', views.quickfire_finish, name='y9_t2_quickfire_result'),
	path('year9/topic3/games/quickfire/result/', views.quickfire_finish, name='y9_t3_quickfire_result'),
	path('year9/topic4/games/quickfire/result/', views.quickfire_finish, name='y9_t4_quickfire_result'),
	path('year9/topic5/games/quickfire/result/', views.quickfire_finish, name='y9_t5_quickfire_result'),
	path('year10/topic1/games/quickfire/result/', views.quickfire_finish, name='y10_t1_quickfire_result'),
	path('year10/topic2/games/quickfire/result/', views.quickfire_finish, name='y10_t2_quickfire_result'),
	path('year10/topic3/games/quickfire/result/', views.quickfire_finish, name='y10_t3_quickfire_result'),
	path('year10/topic4/games/quickfire/result/', views.quickfire_finish, name='y10_t4_quickfire_result'),
	path('year10/topic5/games/quickfire/result/', views.quickfire_finish, name='y10_t5_quickfire_result'),
	path('year11/topic1/games/quickfire/result/', views.quickfire_finish, name='y11_t1_quickfire_result'),
	path('year11/topic2/games/quickfire/result/', views.quickfire_finish, name='y11_t2_quickfire_result'),
	path('year11/topic3/games/quickfire/result/', views.quickfire_finish, name='y11_t3_quickfire_result'),
	path('year11/topic4/games/quickfire/result/', views.quickfire_finish, name='y11_t4_quickfire_result'),
	path('year11/topic5/games/quickfire/result/', views.quickfire_finish, name='y11_t5_quickfire_result'),
]

quickfirepatterns = [
	path('year7/topic1/games/quickfire/', views.start_quickfire, name='y7_t1_quickfire'),
	path('year7/topic2/games/quickfire/', views.start_quickfire, name='y7_t2_quickfire'),
	path('year7/topic3/games/quickfire/', views.start_quickfire, name='y7_t3_quickfire'),
	path('year7/topic4/games/quickfire/', views.start_quickfire, name='y7_t4_quickfire'),
	path('year7/topic5/games/quickfire/', views.start_quickfire, name='y7_t5_quickfire'),
	path('year7/topic6/games/quickfire/', views.start_quickfire, name='y7_t6_quickfire'),
	path('year8/topic1/games/quickfire/', views.start_quickfire, name='y8_t1_quickfire'),
	path('year8/topic2/games/quickfire/', views.start_quickfire, name='y8_t2_quickfire'),
	path('year8/topic3/games/quickfire/', views.start_quickfire, name='y8_t3_quickfire'),
	path('year8/topic4/games/quickfire/', views.start_quickfire, name='y8_t4_quickfire'),
	path('year8/topic5/games/quickfire/', views.start_quickfire, name='y8_t5_quickfire'),
	path('year9/topic1/games/quickfire/', views.start_quickfire, name='y9_t1_quickfire'),
	path('year9/topic2/games/quickfire/', views.start_quickfire, name='y9_t2_quickfire'),
	path('year9/topic3/games/quickfire/', views.start_quickfire, name='y9_t3_quickfire'),
	path('year9/topic4/games/quickfire/', views.start_quickfire, name='y9_t4_quickfire'),
	path('year9/topic5/games/quickfire/', views.start_quickfire, name='y9_t5_quickfire'),
	path('year10/topic1/games/quickfire/', views.start_quickfire, name='y10_t1_quickfire'),
	path('year10/topic2/games/quickfire/', views.start_quickfire, name='y10_t2_quickfire'),
	path('year10/topic3/games/quickfire/', views.start_quickfire, name='y10_t3_quickfire'),
	path('year10/topic4/games/quickfire/', views.start_quickfire, name='y10_t4_quickfire'),
	path('year10/topic5/games/quickfire/', views.start_quickfire, name='y10_t5_quickfire'),
	path('year11/topic1/games/quickfire/', views.start_quickfire, name='y11_t1_quickfire'),
	path('year11/topic2/games/quickfire/', views.start_quickfire, name='y11_t2_quickfire'),
	path('year11/topic3/games/quickfire/', views.start_quickfire, name='y11_t3_quickfire'),
	path('year11/topic4/games/quickfire/', views.start_quickfire, name='y11_t4_quickfire'),
	path('year11/topic5/games/quickfire/', views.start_quickfire, name='y11_t5_quickfire'),
]

hangmanresultpatterns = [
	path('year7/topic1/games/hangman/result/', views.hangman_finish, name='y7_t1_hangman_result'),
	path('year7/topic2/games/hangman/result/', views.hangman_finish, name='y7_t2_hangman_result'),
	path('year7/topic3/games/hangman/result/', views.hangman_finish, name='y7_t3_hangman_result'),
	path('year7/topic4/games/hangman/result/', views.hangman_finish, name='y7_t4_hangman_result'),
	path('year7/topic5/games/hangman/result/', views.hangman_finish, name='y7_t5_hangman_result'),
	path('year7/topic6/games/hangman/result/', views.hangman_finish, name='y7_t6_hangman_result'),
	path('year8/topic1/games/hangman/result/', views.hangman_finish, name='y8_t1_hangman_result'),
	path('year8/topic2/games/hangman/result/', views.hangman_finish, name='y8_t2_hangman_result'),
	path('year8/topic3/games/hangman/result/', views.hangman_finish, name='y8_t3_hangman_result'),
	path('year8/topic4/games/hangman/result/', views.hangman_finish, name='y8_t4_hangman_result'),
	path('year8/topic5/games/hangman/result/', views.hangman_finish, name='y8_t5_hangman_result'),
	path('year9/topic1/games/hangman/result/', views.hangman_finish, name='y9_t1_hangman_result'),
	path('year9/topic2/games/hangman/result/', views.hangman_finish, name='y9_t2_hangman_result'),
	path('year9/topic3/games/hangman/result/', views.hangman_finish, name='y9_t3_hangman_result'),
	path('year9/topic4/games/hangman/result/', views.hangman_finish, name='y9_t4_hangman_result'),
	path('year9/topic5/games/hangman/result/', views.hangman_finish, name='y9_t5_hangman_result'),
	path('year10/topic1/games/hangman/result/', views.hangman_finish, name='y10_t1_hangman_result'),
	path('year10/topic2/games/hangman/result/', views.hangman_finish, name='y10_t2_hangman_result'),
	path('year10/topic3/games/hangman/result/', views.hangman_finish, name='y10_t3_hangman_result'),
	path('year10/topic4/games/hangman/result/', views.hangman_finish, name='y10_t4_hangman_result'),
	path('year10/topic5/games/hangman/result/', views.hangman_finish, name='y10_t5_hangman_result'),
	path('year11/topic1/games/hangman/result/', views.hangman_finish, name='y11_t1_hangman_result'),
	path('year11/topic2/games/hangman/result/', views.hangman_finish, name='y11_t2_hangman_result'),
	path('year11/topic3/games/hangman/result/', views.hangman_finish, name='y11_t3_hangman_result'),
	path('year11/topic4/games/hangman/result/', views.hangman_finish, name='y11_t4_hangman_result'),
	path('year11/topic5/games/hangman/result/', views.hangman_finish, name='y11_t5_hangman_result'),
]

hangmanpatterns = [
	path('year7/topic1/games/hangman/', views.start_hangman, name='y7_t1_hangman'),
	path('year7/topic2/games/hangman/', views.start_hangman, name='y7_t2_hangman'),
	path('year7/topic3/games/hangman/', views.start_hangman, name='y7_t3_hangman'),
	path('year7/topic4/games/hangman/', views.start_hangman, name='y7_t4_hangman'),
	path('year7/topic5/games/hangman/', views.start_hangman, name='y7_t5_hangman'),
	path('year7/topic6/games/hangman/', views.start_hangman, name='y7_t6_hangman'),
	path('year8/topic1/games/hangman/', views.start_hangman, name='y8_t1_hangman'),
	path('year8/topic2/games/hangman/', views.start_hangman, name='y8_t2_hangman'),
	path('year8/topic3/games/hangman/', views.start_hangman, name='y8_t3_hangman'),
	path('year8/topic4/games/hangman/', views.start_hangman, name='y8_t4_hangman'),
	path('year8/topic5/games/hangman/', views.start_hangman, name='y8_t5_hangman'),
	path('year9/topic1/games/hangman/', views.start_hangman, name='y9_t1_hangman'),
	path('year9/topic2/games/hangman/', views.start_hangman, name='y9_t2_hangman'),
	path('year9/topic3/games/hangman/', views.start_hangman, name='y9_t3_hangman'),
	path('year9/topic4/games/hangman/', views.start_hangman, name='y9_t4_hangman'),
	path('year9/topic5/games/hangman/', views.start_hangman, name='y9_t5_hangman'),
	path('year10/topic1/games/hangman/', views.start_hangman, name='y10_t1_hangman'),
	path('year10/topic2/games/hangman/', views.start_hangman, name='y10_t2_hangman'),
	path('year10/topic3/games/hangman/', views.start_hangman, name='y10_t3_hangman'),
	path('year10/topic4/games/hangman/', views.start_hangman, name='y10_t4_hangman'),
	path('year10/topic5/games/hangman/', views.start_hangman, name='y10_t5_hangman'),
	path('year11/topic1/games/hangman/', views.start_hangman, name='y11_t1_hangman'),
	path('year11/topic2/games/hangman/', views.start_hangman, name='y11_t2_hangman'),
	path('year11/topic3/games/hangman/', views.start_hangman, name='y11_t3_hangman'),
	path('year11/topic4/games/hangman/', views.start_hangman, name='y11_t4_hangman'),
	path('year11/topic5/games/hangman/', views.start_hangman, name='y11_t5_hangman'),
]

anagramresultpatterns = [
	path('year7/topic1/games/anagrams/result/', views.anagram_finish, name='y7_t1_anagram_result'),
	path('year7/topic2/games/anagrams/result/', views.anagram_finish, name='y7_t2_anagram_result'),
	path('year7/topic3/games/anagrams/result/', views.anagram_finish, name='y7_t3_anagram_result'),
	path('year7/topic4/games/anagrams/result/', views.anagram_finish, name='y7_t4_anagram_result'),
	path('year7/topic5/games/anagrams/result/', views.anagram_finish, name='y7_t5_anagram_result'),
	path('year7/topic6/games/anagrams/result/', views.anagram_finish, name='y7_t6_anagram_result'),
	path('year8/topic1/games/anagrams/result/', views.anagram_finish, name='y8_t1_anagram_result'),
	path('year8/topic2/games/anagrams/result/', views.anagram_finish, name='y8_t2_anagram_result'),
	path('year8/topic3/games/anagrams/result/', views.anagram_finish, name='y8_t3_anagram_result'),
	path('year8/topic4/games/anagrams/result/', views.anagram_finish, name='y8_t4_anagram_result'),
	path('year8/topic5/games/anagrams/result/', views.anagram_finish, name='y8_t5_anagram_result'),
	path('year9/topic1/games/anagrams/result/', views.anagram_finish, name='y9_t1_anagram_result'),
	path('year9/topic2/games/anagrams/result/', views.anagram_finish, name='y9_t2_anagram_result'),
	path('year9/topic3/games/anagrams/result/', views.anagram_finish, name='y9_t3_anagram_result'),
	path('year9/topic4/games/anagrams/result/', views.anagram_finish, name='y9_t4_anagram_result'),
	path('year9/topic5/games/anagrams/result/', views.anagram_finish, name='y9_t5_anagram_result'),
	path('year10/topic1/games/anagrams/result/', views.anagram_finish, name='y10_t1_anagram_result'),
	path('year10/topic2/games/anagrams/result/', views.anagram_finish, name='y10_t2_anagram_result'),
	path('year10/topic3/games/anagrams/result/', views.anagram_finish, name='y10_t3_anagram_result'),
	path('year10/topic4/games/anagrams/result/', views.anagram_finish, name='y10_t4_anagram_result'),
	path('year10/topic5/games/anagrams/result/', views.anagram_finish, name='y10_t5_anagram_result'),
	path('year11/topic1/games/anagrams/result/', views.anagram_finish, name='y11_t1_anagram_result'),
	path('year11/topic2/games/anagrams/result/', views.anagram_finish, name='y11_t2_anagram_result'),
	path('year11/topic3/games/anagrams/result/', views.anagram_finish, name='y11_t3_anagram_result'),
	path('year11/topic4/games/anagrams/result/', views.anagram_finish, name='y11_t4_anagram_result'),
	path('year11/topic5/games/anagrams/result/', views.anagram_finish, name='y11_t5_anagram_result'),
]

anagrampatterns = [
	path('year7/topic1/games/anagrams/', views.start_anagram, name='y7_t1_anagram'),
	path('year7/topic2/games/anagrams/', views.start_anagram, name='y7_t2_anagram'),
	path('year7/topic3/games/anagrams/', views.start_anagram, name='y7_t3_anagram'),
	path('year7/topic4/games/anagrams/', views.start_anagram, name='y7_t4_anagram'),
	path('year7/topic5/games/anagrams/', views.start_anagram, name='y7_t5_anagram'),
	path('year7/topic6/games/anagrams/', views.start_anagram, name='y7_t6_anagram'),
	path('year8/topic1/games/anagrams/', views.start_anagram, name='y8_t1_anagram'),
	path('year8/topic2/games/anagrams/', views.start_anagram, name='y8_t2_anagram'),
	path('year8/topic3/games/anagrams/', views.start_anagram, name='y8_t3_anagram'),
	path('year8/topic4/games/anagrams/', views.start_anagram, name='y8_t4_anagram'),
	path('year8/topic5/games/anagrams/', views.start_anagram, name='y8_t5_anagram'),
	path('year9/topic1/games/anagrams/', views.start_anagram, name='y9_t1_anagram'),
	path('year9/topic2/games/anagrams/', views.start_anagram, name='y9_t2_anagram'),
	path('year9/topic3/games/anagrams/', views.start_anagram, name='y9_t3_anagram'),
	path('year9/topic4/games/anagrams/', views.start_anagram, name='y9_t4_anagram'),
	path('year9/topic5/games/anagrams/', views.start_anagram, name='y9_t5_anagram'),
	path('year10/topic1/games/anagrams/', views.start_anagram, name='y10_t1_anagram'),
	path('year10/topic2/games/anagrams/', views.start_anagram, name='y10_t2_anagram'),
	path('year10/topic3/games/anagrams/', views.start_anagram, name='y10_t3_anagram'),
	path('year10/topic4/games/anagrams/', views.start_anagram, name='y10_t4_anagram'),
	path('year10/topic5/games/anagrams/', views.start_anagram, name='y10_t5_anagram'),
	path('year11/topic1/games/anagrams/', views.start_anagram, name='y11_t1_anagram'),
	path('year11/topic2/games/anagrams/', views.start_anagram, name='y11_t2_anagram'),
	path('year11/topic3/games/anagrams/', views.start_anagram, name='y11_t3_anagram'),
	path('year11/topic4/games/anagrams/', views.start_anagram, name='y11_t4_anagram'),
	path('year11/topic5/games/anagrams/', views.start_anagram, name='y11_t5_anagram'),
]

gameselectpattern = [
	path('games/', views.gameselect, name= 'gameselect'),
]

nogamespattern = [
	path('games/', views.nogamesview, name= 'nogames')
]

urlpatterns = [
	path('year7/topic1/', include(gameselectpattern)),
	path('year7/topic2/', include(gameselectpattern)),
	path('year7/topic3/', include(gameselectpattern)),
	path('year7/topic4/', include(gameselectpattern)),
	path('year7/topic5/', include(gameselectpattern)),
	path('year7/topic6/', include(gameselectpattern)),
	path('year8/topic1/', include(gameselectpattern)),
	path('year8/topic2/', include(gameselectpattern)),
	path('year8/topic3/', include(nogamespattern)),
	path('year8/topic4/', include(gameselectpattern)),
	path('year8/topic5/', include(gameselectpattern)),
	path('year9/topic1/', include(gameselectpattern)),
	path('year9/topic2/', include(gameselectpattern)),
	path('year9/topic3/', include(gameselectpattern)),
	path('year9/topic4/', include(gameselectpattern)),
	path('year9/topic5/', include(nogamespattern)),
	path('year10/topic1/', include(gameselectpattern)),
	path('year10/topic2/', include(gameselectpattern)),
	path('year10/topic3/', include(nogamespattern)),
	path('year10/topic4/', include(gameselectpattern)),
	path('year10/topic5/', include(nogamespattern)),
	path('year11/topic1/', include(gameselectpattern)),
	path('year11/topic2/', include(nogamespattern)),
	path('year11/topic3/', include(gameselectpattern)),
	path('year11/topic4/', include(gameselectpattern)),
	path('year11/topic5/', include(gameselectpattern)),
	path('', include(anagrampatterns)),
	path('', include(anagramresultpatterns)),
	path('', include(hangmanpatterns)),
	path('', include(hangmanresultpatterns)),
	path('', include(quickfirepatterns)),
	path('', include(quickfireresultpatterns)),
]