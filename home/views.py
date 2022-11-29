from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from login import models, forms
from login.models import TME_002_User, Víctima, Solicitante_Externo, Denuncia, Servidor_Público
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url = 'login:login')
def home_servidor(request):
    return render(request, 'home_servidor.html')

@login_required(login_url = 'login:login')
def home_victima(request):
    return render (request, 'home_victima.html')

@login_required(login_url = 'login:login')
def home_solicitante(request):
    return render (request, 'home_solicitante.html')

