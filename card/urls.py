from . import views
from django.urls import path

urlpatterns = [
    path('cards/', views.cards),
]
