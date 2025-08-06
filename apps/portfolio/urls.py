from django.urls import path, re_path
from .views import project_list, project_detail

app_name = 'portfolio' # تعریف یک نام برای این مجموعه از URLها

urlpatterns = [
    path('projects/', project_list, name='project-list'),
    re_path(r'^projects/(?P<slug>[-\w\u0600-\u06FF]+)/$', project_detail, name='project-detail')
]