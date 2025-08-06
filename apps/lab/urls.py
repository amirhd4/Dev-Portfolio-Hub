from django.urls import path
from .views import lab_home

app_name = 'lab'

urlpatterns = [
    path('lab/', lab_home, name='lab-home'),
]