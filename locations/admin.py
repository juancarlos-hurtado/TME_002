from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Entidad_Federativa, Alcaldia, Colonia


admin.site.register(Entidad_Federativa)
admin.site.register(Colonia)
admin.site.register(Alcaldia)

