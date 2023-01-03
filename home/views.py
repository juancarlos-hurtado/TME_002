from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from login import models, forms
from login.models import TME_002_User, Víctima, Solicitante_Externo, Servidor_Público, Coordinador, Trabajador_Social, Psicologo, Medico
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url = 'login:login')
def home_servidor(request):
    return render(request, 'home/home_servidor.html')

@login_required(login_url = 'login:login')
def home_victima(request):
    return render (request, 'home/home_victima.html')

@login_required(login_url = 'login:login')
def home_solicitante(request):
    return render (request, 'home/home_solicitante.html')

@login_required(login_url = 'login:login')
def home_coordinador(request):
    return render (request, 'home/home_coordinador.html')

@login_required(login_url = 'login:login')
def home_trabajador(request):
    return render(request, 'home/home_trabajador.html')

@login_required(login_url = 'login:login')
def registrar_equipo(request):
    context = {
        'select_coordinador': Coordinador.objects.all(),
        'select_trabajador': Trabajador_Social.objects.all(),
        'select_psicologo': Psicologo.objects.all(),
        'select_medico': Medico.objects.all()
    }
    return render (request, 'home/registrar_equipo.html', context)

