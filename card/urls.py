from . import views
from django.urls import path

app_name = 'card'

urlpatterns = [
    path('cards/', views.cards, name='cards'),
]
