from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from . import forms, models
from .models import TME_002_User, Víctima, Solicitante_Externo, Denuncia, Servidor_Público
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    context = {
        'login_form' : forms.login_form(),
        'create_form' : forms.create_form(),
        'forgot_form' : forms.forgot_form(),
    }
    
    if request.method == 'POST':

        if 'save_user' in request.POST:
            context['login_form'] = forms.login_form(request.POST)
            if context['login_form'].is_valid():
                username = request.POST['username']
                password =  request.POST['password']

                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('login:home')
                else:
                    messages.error(request, 'Usuario o contraseña inválida.')

        if 'save_account' in request.POST:
            context['create_form'] = forms.create_form(request.POST)
            if context['create_form'].is_valid:
                username = request.POST['create_username']
                email = request.POST['create_email']
                password = request.POST['create_password']
                user_type = request.POST['create_user_type']
                account = TME_002_User.objects.create_user(username, email, password, user_type = user_type)
                

                user = authenticate(request, username = username, password = password)

                login(request, user)

                return redirect('login:home')

    return render(request, 'login/base.html', context)

@login_required(login_url = 'login:login')
def home(request):
    if request.user.is_profiled == True:
        if request.user.user_type == 'Víctima':
            return redirect('home:home-victima')
        elif request.user.user_type == 'Solicitante Externo':
            return redirect('home:home-solicitante')
        else:
            return redirect('home:home-servidor')
    else:
        if request.user.user_type == 'Víctima':
            return redirect('login:complete_victim_profile')
        elif request.user.user_type == 'Solicitante Externo':
            return redirect('login:complete_solicitante_profile')
        else:
            return redirect('login:complete_servidor_profile')

@login_required(login_url = 'login:login')
def complete_victim_profile(request):
    context = {
        'user_type' : request.user.user_type
    }
    if request.method == 'POST':
        if 'finalizar' in request.POST:
            tipo = request.POST['tipo']
            nombres = request.POST['nombres']
            primer_apellido = request.POST['primer_apellido']
            segundo_apellido = request.POST['segundo_apellido']
            fecha_nacimiento = request.POST.get('fecha_nacimiento')
            sexo = request.POST['sexo']
            nacionalidad = request.POST['nacionalidad']
            curp = request.POST['curp']
            pais_nacimiento = request.POST['país']
            entidad_nacimiento = request.POST['ent_fed_nac']
            del_mun_nac = request.POST['del_mun_nac']
            com_nacimiento = request.POST['comunidad_nacimiento']
            estado_civil = request.POST['edo_civil']
            calle = request.POST['calle']
            num_exterior = request.POST['num_exterior']
            num_interior = request.POST['num_interior']
            cp = request.POST['cp']
            colonia = request.POST['colonia']
            localidad = request.POST['localidad']
            del_mun = request.POST['del_mun']
            entidad_federativa = request.POST['ent_fed']
            telefono = request.POST['teléfono']
            email_victima = request.POST['email']

            User = get_user_model()
            user = User.objects.get(id=request.user.id)
            
            push_to_victima = Víctima.objects.create(víctima = user, tipo = tipo, fecha_de_nacimiento = fecha_nacimiento, sexo = sexo, nacionalidad = nacionalidad, curp = curp, pais_nacimiento = pais_nacimiento, entidad_nacimiento = entidad_nacimiento, del_mun_nac = del_mun_nac, comunidad_nacimiento = com_nacimiento, estado_civil = estado_civil, calle = calle, num_exterior = num_exterior, num_interior = num_interior, cp = cp, colonia = colonia, localidad = localidad, del_mun = del_mun, entidad_federativa = entidad_federativa, tel = telefono, email_victima = email_victima)
            push_to_victima.save()
            
            user.nombres = nombres
            user.primer_apellido = primer_apellido
            user.segundo_apellido = segundo_apellido
            user.save()
            user.is_profiled = True
            user.save()
            
            return redirect('login:home')

    return render (request, 'login/complete_victim_profile.html', context)

@login_required(login_url = 'login:login')
def complete_solicitante_profile(request):
    context = {
        'user_type': request.user.user_type
    }

    if request.method == 'POST':
        if 'finalizar' in request.POST:
            User = get_user_model()
            user = User.objects.get(id=request.user.id)

            nombres = request.POST['nombres']
            primer_apellido = request.POST['primer_apellido']
            segundo_apellido = request.POST['segundo_apellido']
            parentesco = request.POST['parentesco']
            tel_movil = request.POST['tel_movil']
            tel_fijo = request.POST['tel_fijo']
            email = request.POST['email']
            otros_datos = request.POST['otros_datos']

            push_to_solicitante = Solicitante_Externo.objects.create(solicitante = user, parentesco = parentesco, tel_movil = tel_movil, tel_fijo = tel_fijo, email = email, otros_datos_contacto = otros_datos)
            user.nombres = nombres
            user.primer_apellido = primer_apellido
            user.segundo_apellido = segundo_apellido
            user.save()
            push_to_solicitante.save()
            user.is_profiled = True
            user.save()

            return redirect('login:home')
            
    return render(request, 'login/complete_solicitante_profile.html', context )

@login_required(login_url = 'login:login')
def complete_servidor_profile(request):
    context = {
        'user_type' : request.user.user_type
    }
    if request.method == 'POST':
        if 'finalizar' in request.POST:
            User = get_user_model()
            user = User.objects.get(id=request.user.id)

            nombres = request.POST['nombres']
            primer_apellido = request.POST['primer_apellido']
            segundo_apellido = request.POST['segundo_apellido']
            servidor = user
            institucion = request.POST['dependencia']
            cargo = request.POST['cargo']
            tel_movil = request.POST['tel_movil']
            tel_fijo = request.POST['tel_fijo']
            email = request.POST['email']

            push_to_servidor = Servidor_Público.objects.create(servidor = user, institucion = institucion, cargo = cargo, tel_movil = tel_movil, tel_fijo = tel_fijo, email = email)
            push_to_servidor.save()

            user.nombres = nombres
            user.primer_apellido = primer_apellido
            user.segundo_apellido = segundo_apellido
            user.is_profiled = True
            user.save()
            
            return redirect('login:home')

    return render(request, 'login/complete_servidor_profile.html', context )

@login_required
def logout_user(request):
    logout(request)
    return redirect('login:login')