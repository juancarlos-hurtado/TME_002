from django.db import models
from django.contrib.auth.models import AbstractUser
from dataclasses import dataclass
from locations import models as mdl

class TME_002_User(AbstractUser):
    nombres = models.CharField(max_length = 100, null = True, blank = True)
    primer_apellido = models.CharField(max_length = 100, null = True, blank = True)
    segundo_apellido = models.CharField(max_length = 100, null = True, blank = True)
    user_type = models.CharField(max_length = 25)
    is_profiled = models.BooleanField(default = False)


class Víctima(models.Model):
    víctima = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    tipo = models.CharField(max_length = 10)
    fecha_de_nacimiento = models.DateField(auto_now = False, auto_now_add = False)
    sexo = models.CharField(max_length = 10)
    nacionalidad = models.CharField(max_length = 20, null = True, blank = True)
    curp = models.CharField(max_length = 18)
    pais_nacimiento = models.CharField(max_length = 50, null = True, blank = True)
    entidad_nacimiento = models.ForeignKey(mdl.Entidad_Federativa, null = True, on_delete = models.CASCADE, related_name = 'entidad_nacimiento')
    #entidad_nacimiento = models.CharField(max_length = 50, null = True, blank = True)
    del_mun_nac = models.CharField(max_length = 50, null = True, blank = True)
    comunidad_nacimiento = models.CharField(max_length = 50, null = True, blank = True)
    estado_civil = models.CharField(max_length = 20)
    calle = models.CharField(max_length = 100)
    num_exterior = models.CharField(max_length = 10)
    num_interior = models.CharField(max_length = 10, null = True, blank = True)
    cp = models.CharField(max_length = 10)
    colonia = models.ForeignKey(mdl.Colonia, null = True, blank = True, on_delete = models.CASCADE)
    localidad = models.CharField(max_length = 100, null = True, blank = True)
    del_mun = models.ForeignKey(mdl.Alcaldia, null = True, blank = True, on_delete = models.CASCADE)
    entidad_federativa = models.ForeignKey(mdl.Entidad_Federativa, null = True, on_delete = models.CASCADE, related_name = 'entidad_federativa')
    #entidad_federativa = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 20, null = True, blank = True)
    email_victima = models.EmailField(max_length = 254, null = True, blank = True)
    coordinador_asignado = models.ForeignKey('Coordinador', null = True, blank = True, on_delete = models.CASCADE)
    trabajador_asignado = models.ForeignKey('Trabajador_Social', null = True, blank = True, on_delete = models.CASCADE)
    psicologo_asignado = models.ForeignKey('Psicologo', null = True, blank = True, on_delete = models.CASCADE)
    medico_asignado = models.ForeignKey('Medico', null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return (self.víctima.nombres + ' ' +self.víctima.primer_apellido + ' ' + self.víctima.segundo_apellido)

class Solicitante_Externo(models.Model):
    solicitante = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    parentesco = models.CharField(max_length = 100)
    tel_movil = models.CharField(max_length = 20, null = True, blank = True)
    tel_fijo = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(max_length = 254, null = True, blank = True)
    otros_datos_contacto = models.TextField(null = True, blank = True)

    def __str__(self):
        return (self.solicitante.nombres + ' ' + self.solicitante.primer_apellido + ' ' + self.solicitante.segundo_apellido)

class Servidor_Público(models.Model):
    servidor = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    institucion = models.CharField(max_length = 100)
    cargo = models.CharField(max_length = 100)
    tel_movil = models.CharField(max_length = 20, null = True, blank = True)
    tel_fijo = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(max_length = 254, null = True, blank = True)

    def __str__(self):
        return(self.servidor.nombres + ' ' + self.servidor.primer_apellido + ' ' + self.servidor.segundo_apellido)


class Coordinador(models.Model):
    coordinador = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    tel_movil = models.CharField(max_length = 20, null = True, blank = True)
    tel_fijo = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(max_length = 254, null = True, blank = True)

    def __str__(self):
        return(self.coordinador.nombres + ' ' + self.coordinador.primer_apellido + ' ' + self.coordinador.segundo_apellido)

class Trabajador_Social(models.Model):
    trabajador_social = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    tel_movil = models.CharField(max_length = 20, null = True, blank = True)
    tel_fijo = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(max_length = 254, null = True, blank = True)

    def __str__(self):
        return (self.trabajador_social.nombres + ' ' + self.trabajador_social.primer_apellido + ' ' + self.trabajador_social.segundo_apellido)

class Psicologo(models.Model):
    psicologo = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    tel_movil = models.CharField(max_length = 20, null = True, blank = True)
    tel_fijo = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(max_length = 254, null = True, blank = True)

    def __str__(self):
        return (self.psicologo.nombres + ' ' + self.psicologo.primer_apellido + ' ' + self.psicologo.segundo_apellido)

class Medico(models.Model):
    medico = models.OneToOneField(TME_002_User, primary_key = True, on_delete = models.CASCADE)
    tel_movil = models.CharField(max_length = 20, null = True, blank = True)
    tel_fijo = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(max_length = 254, null = True, blank = True)

    def __str__(self):
        return (self.medico.nombres + ' ' + self.medico.primer_apellido + ' ' + self.medico.segundo_apellido)