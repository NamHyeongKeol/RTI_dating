from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_change, password_change_done, login
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm

from .views import signup, signin

urlpatterns = [
    # url('change-password/', auth_views.PasswordChangeView.as_view()),
    path('login', login, {'template_name' : 'admin/login.html'}),
    path('join', signup),
    path('password_change', password_change, {'template_name': 'admin/login.html'}), # , {'password_change_form': PasswordChangeForm}
    path('password_change/done', password_change_done, name='password_change_done')
]
