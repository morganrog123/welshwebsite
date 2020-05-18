# URL path configuration
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='welsh/index.html'), name='index'),
    path('home/', views.home, name='home'),
    path('year7/', views.year7, name='year_7'),
	path('year8/', views.year8, name='year_8'),
	path('year9/', views.year9, name='year_9'),
	path('year10/', views.year10, name='year_10'),
	path('year11/', views.year11, name='year_11'),
]