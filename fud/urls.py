from django.urls import path
from . import views

app_name = 'fud'

urlpatterns = [
    path('registrar-denuncia-victima', views.registrar_denuncia_víctima, name = 'registrar-denuncia-victima')
]