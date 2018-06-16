from django.urls import path
from . import views

urlpatterns = [
    path('base_site/', views.base_site),
]
