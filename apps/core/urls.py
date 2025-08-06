from django.urls import path
from . import views
from .views import contact_success_view, contact_view


app_name = "core"


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact-success'),
]