# URL path configuration
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

topicpatterns = [
	path('topic1/', views.selectview, name='topic_1'),
	path('topic2/', views.selectview, name='topic_2'),
	path('topic3/', views.selectview, name='topic_3'),
	path('topic4/', views.selectview, name='topic_4'),
	path('topic5/', views.selectview, name='topic_5'),
]

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='welsh/index.html'), name='index'),
    path('home/', views.home, name='home'),
    path('year7/', views.year7, name='year_7'),
	path('year8/', views.year8, name='year_8'),
	path('year9/', views.year9, name='year_9'),
	path('year10/', views.year10, name='year_10'),
	path('year11/', views.year11, name='year_11'),
    path('year7/', include(topicpatterns)),
    path('year8/', include(topicpatterns)),
    path('year9/', include(topicpatterns)),
    path('year10/', include(topicpatterns)),
    path('year11/', include(topicpatterns)),
    path('year7/topic6/', views.selectview, name='y7_topic_6'),
]