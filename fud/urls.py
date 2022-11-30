from django.urls import path
from . import views

app_name = 'fud'

urlpatterns = [
    path('registrar-denuncia-victima', views.registrar_denuncia_víctima, name = 'registrar-denuncia-victima'),
    path('registrar-denuncia-solicitante', views.registrar_denuncia_solicitante, name = 'registrar-denuncia-solicitante'),
    path('complete-victim-profile', views.registrar_victima, name = 'complete-victim-profile'),
    path('registrar-denuncia-servidor', views.registrar_denuncia_servidor, name = 'registrar-denuncia-servidor')
]