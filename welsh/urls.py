# URL path configuration
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]