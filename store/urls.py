from . import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('store/', views.store, name='store'),
]
