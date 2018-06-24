from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('store/', views.home, name='store'),
]
