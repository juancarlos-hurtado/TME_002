from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from login import forms, models
from login.models import TME_002_User, Víctima, Solicitante_Externo, Servidor_Público
from django.contrib.auth.models import User
from .models import Denuncia

# Create your views here.
@login_required(login_url='login:login')
def registrar_denuncia_víctima(request):
    if request.method == 'POST':
        if 'enviar_denuncia' in request.POST:
            User = get_user_model()
            user = User.objects.get(id=request.user.id)

            tipo_de_daño = request.POST['tipo_daño']
            denunciante = user
            víctima = models.Víctima.objects.get(víctima = request.user.id)
            fecha_hechos = request.POST['fecha_hechos']
            calle = request.POST['calle']
            número_exterior = request.POST['num_exterior']
            número_interior = request.POST['num_interior']
            código_postal = request.POST['cp']
            colonia = request.POST['colonia']
            localidad = request.POST['localidad']
            del_mun = request.POST['del_mun']
            entidad_federativa = request.POST['entidad_federativa']
            otros_datos = request.POST['otros_datos']
            relato = request.POST['relato_hechos']

            push_to_denuncia = Denuncia.objects.create(tipo_de_daño = tipo_de_daño, denunciante = denunciante, víctima = víctima, fecha_hechos = fecha_hechos, calle = calle, número_exterior = número_exterior, número_interior = número_interior, código_postal = código_postal, colonia = colonia, localidad = localidad, del_mun = del_mun, entidad_federativa = entidad_federativa, otros_datos_ubicación = otros_datos, relato_de_hechos = relato)
            push_to_denuncia.save()

            return redirect('login:home')

    return render(request, 'fud/registrar_denuncia.html')

@login_required(login_url = 'login:login')
def registrar_denuncia_solicitante(request):
    if request.method == 'POST':
        if 'enviar_denuncia' in request.POST:
            User = get_user_model()
            user = User.objects.get(id = request.user.id)

            tipo_de_daño = request.POST['tipo_daño']
            denunciante = user
            curp_víctima = request.POST['buscar_curp']
            fecha_hechos = request.POST['fecha_hechos']
            calle = request.POST['calle']
            número_exterior = request.POST['num_exterior']
            número_interior = request.POST['num_interior']
            código_postal = request.POST['cp']
            colonia = request.POST['colonia']
            localidad = request.POST['localidad']
            del_mun = request.POST['del_mun']
            entidad_federativa = request.POST['entidad_federativa']
            otros_datos = request.POST['otros_datos']
            relato = request.POST['relato_hechos']
            víctima = Víctima.objects.get(curp = curp_víctima)
            print(víctima)
            push_to_denuncia = Denuncia.objects.create(tipo_de_daño = tipo_de_daño, denunciante = denunciante, víctima = víctima, fecha_hechos = fecha_hechos, calle = calle, número_exterior = número_exterior, número_interior = número_interior, código_postal = código_postal, colonia = colonia, localidad = localidad, del_mun = del_mun, entidad_federativa = entidad_federativa, otros_datos_ubicación = otros_datos, relato_de_hechos = relato)
            push_to_denuncia.save()

    return render(request, 'fud/registrar_denunciav2.html')

@login_required(login_url = 'login:login')
def registrar_denuncia_servidor(request):
    if request.method == 'POST':
        if 'enviar_denuncia' in request.POST:
            User = get_user_model()
            user = User.objects.get(id = request.user.id)

            tipo_de_daño = request.POST['tipo_daño']
            denunciante = user
            curp_víctima = request.POST['buscar_curp']
            fecha_hechos = request.POST['fecha_hechos']
            calle = request.POST['calle']
            número_exterior = request.POST['num_exterior']
            número_interior = request.POST['num_interior']
            código_postal = request.POST['cp']
            colonia = request.POST['colonia']
            localidad = request.POST['localidad']
            del_mun = request.POST['del_mun']
            entidad_federativa = request.POST['entidad_federativa']
            otros_datos = request.POST['otros_datos']
            relato = request.POST['relato_hechos']
            víctima = Víctima.objects.get(curp = curp_víctima)
            print(víctima)
            
            push_to_denuncia = Denuncia.objects.create(tipo_de_daño = tipo_de_daño, denunciante = denunciante, víctima = víctima, fecha_hechos = fecha_hechos, calle = calle, número_exterior = número_exterior, número_interior = número_interior, código_postal = código_postal, colonia = colonia, localidad = localidad, del_mun = del_mun, entidad_federativa = entidad_federativa, otros_datos_ubicación = otros_datos, relato_de_hechos = relato)
            push_to_denuncia.save()
            
    return render(request, 'fud/registrar_denunciav2.html')

@login_required(login_url = 'login:login')
def registrar_victima(request):
    # falta código para contraseña y username temporal
    return render(request, 'fud/complete_victim_profile.html')