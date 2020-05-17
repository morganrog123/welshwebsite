"""welshsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('welsh.urls')),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('myinfo/', accounts_views.myinfo, name='myinfo'),
    path('editinfo/', accounts_views.editinfo, name='editinfo'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/passwordreset.html'), name='passwordreset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/passwordreset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/passwordreset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/passwordreset_complete.html'), name='password_reset_complete'),
    path('changepassword/', accounts_views.change_password, name='change_password'),
    path('admin/', admin.site.urls),

]
