from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import signup, signin

urlpatterns = [
    url('change-password/', auth_views.PasswordChangeView.as_view()),
    url('login', signin, name='login'),
    url('join', signup, name='index')
]