from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_user, name = 'login'),
    path('home', views.home, name = 'home'),
    path('complete-profile', views.complete_victim_profile, name = 'complete_victim_profile'),
    path('complete-profile-solicitante', views.complete_solicitante_profile, name = 'complete_solicitante_profile'),
    path('coplete-servidor-profile', views.complete_servidor_profile, name = 'complete_servidor_profile'),
    path('registrar-denucnia-servidor', views.registrar_denuncia_servidor, name = 'registrar_denuncia_servidor'),
    path('logout', views.logout_user, name = 'logout')
]