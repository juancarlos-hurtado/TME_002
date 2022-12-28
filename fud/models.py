from django.db import models
from django.contrib.auth.models import AbstractUser
from login import models as mdl

class Denuncia(models.Model):
    folio = models.BigAutoField(primary_key=True)
    tipo_de_daño = models.CharField(max_length=20)
    denunciante = models.ForeignKey(mdl.TME_002_User, on_delete = models.CASCADE)
    víctima = models.ForeignKey(mdl.Víctima, on_delete = models.CASCADE)
    estatus = models.CharField(max_length = 20, default = 'En proceso')
    fecha_hechos = models.DateField(auto_now = False, auto_now_add = False)
    calle = models.CharField(max_length = 100, null = True, blank = True)
    número_exterior = models.CharField(max_length = 10, null = True, blank = True)
    número_interior = models.CharField(max_length = 10, null = True, blank = True)
    código_postal = models.CharField(max_length = 10, null = True, blank = True)
    colonia = models.CharField(max_length =100, null = True, blank = True)
    localidad = models.CharField(max_length = 100, null = True, blank = True)
    del_mun = models.CharField(max_length = 100, null = True, blank = True)
    entidad_federativa = models.ForeignKey(mdl.Entidad_Federativa, null = True, on_delete = models.CASCADE, related_name = 'entidad_federativa_denuncia')
    #entidad_federativa = models.CharField(max_length = 100, null = True, blank = True)
    otros_datos_ubicación = models.CharField(max_length = 500, null = True, blank = True)
    relato_de_hechos = models.TextField()

    def __str__(self):
        return ('Folio ' + str(self.folio))