from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TME_002_User, Solicitante_Externo, Servidor_Público, Víctima, Coordinador, Trabajador_Social, Colonia, Entidad_Federativa, Alcaldia

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields' : ('nombres', 'primer_apellido', 'segundo_apellido', 'user_type', 'first_name', 'last_name', 'email', 'is_profiled')})

UserAdmin.fieldsets = tuple(fields)

admin.site.register(TME_002_User, UserAdmin)
admin.site.register(Víctima)
admin.site.register(Solicitante_Externo)
admin.site.register(Servidor_Público)
admin.site.register(Coordinador)
admin.site.register(Trabajador_Social)
admin.site.register(Entidad_Federativa)
admin.site.register(Colonia)
admin.site.register(Alcaldia)

