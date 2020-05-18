# URL path configuration
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='welsh/home.html'), name='index'),
    path('welcome/', views.welcome, name='welcome'),
]