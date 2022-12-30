from django.db import models

class Entidad_Federativa(models.Model):
    nombre = models.CharField(primary_key = True, max_length = 50)
    clave = models.CharField(max_length = 3, null = True, blank = True)

    def __str__(self):
        return(self.nombre)

class Colonia(models.Model):
    cp = models.CharField(max_length = 6, null = True, blank = True)
    colonia = models.CharField(max_length = 150, null = True, blank = True)
    alcaldia = models.ForeignKey('Alcaldia', null = True, blank = True, on_delete = models.CASCADE)
    estado = models.ForeignKey('Entidad_Federativa', null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return(self.colonia)

class Alcaldia(models.Model):
    nombre = models.CharField(primary_key = True, max_length = 50)
    latitud = models.FloatField(null = True, blank = True)
    longitud = models.FloatField(null = True, blank = True)

    def __str__(self):
        return(self.nombre)