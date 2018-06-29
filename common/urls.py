from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
