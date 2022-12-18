from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home-victima', views.home_victima, name = 'home-victima'),
    path('home-servidor', views.home_servidor, name = 'home-servidor'),
    path('home-solicitante', views.home_solicitante, name = 'home-solicitante'),
    path('home-coordinador', views.home_coordinador, name = 'home-coordinador')
]