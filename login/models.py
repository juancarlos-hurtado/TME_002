from django.db import models
from django.contrib.auth.models import AbstractUser

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
    entidad_nacimiento = models.CharField(max_length = 50, null = True, blank = True)
    del_mun_nac = models.CharField(max_length = 50, null = True, blank = True)
    comunidad_nacimiento = models.CharField(max_length = 50, null = True, blank = True)
    estado_civil = models.CharField(max_length = 20)
    calle = models.CharField(max_length = 100)
    num_exterior = models.CharField(max_length = 10)
    num_interior = models.CharField(max_length = 10, null = True, blank = True)
    cp = models.CharField(max_length = 10)
    colonia = models.CharField(max_length = 100)
    localidad = models.CharField(max_length = 100, null = True, blank = True)
    del_mun = models.CharField(max_length = 100)
    entidad_federativa = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 20, null = True, blank = True)
    email_victima = models.EmailField(max_length = 254, null = True, blank = True)

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

class Denuncia(models.Model):
    folio = models.BigAutoField(primary_key = True)
    tipo_de_daño = models.CharField(max_length = 20)
    denunciante = models.ForeignKey(TME_002_User, on_delete = models.CASCADE)
    víctima = models.ForeignKey(Víctima, on_delete = models.CASCADE)
    estatus = models.CharField(max_length = 20, default = 'En proceso')
    fecha_hechos = models.DateField(auto_now = False, auto_now_add = False)
    calle = models.CharField(max_length = 100, null = True, blank = True)
    número_exterior = models.CharField(max_length = 10, null = True, blank = True)
    número_interior = models.CharField(max_length = 10, null = True, blank = True)
    código_postal = models.CharField(max_length = 10, null = True, blank = True)
    colonia = models.CharField(max_length = 100, null = True, blank = True)
    localidad = models.CharField(max_length = 100, null = True, blank = True)
    del_mun = models.CharField(max_length = 100, null = True, blank = True)
    entidad_federativa = models.CharField(max_length = 100, null = True, blank = True)
    otros_datos_ubicación = models.CharField(max_length = 100, null = True, blank = True)
    relato_de_hechos = models.TextField()

    def __str__(self):
        return ('Folio ' + str(self.folio))