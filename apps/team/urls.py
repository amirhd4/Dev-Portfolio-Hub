from django.urls import path
from .views import team_list

app_name = 'team'

urlpatterns = [
    path('team/', team_list, name='team-list'),
]