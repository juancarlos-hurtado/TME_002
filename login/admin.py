from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TME_002_User, Solicitante_Externo, Servidor_Público, Víctima

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields' : ('nombres', 'primer_apellido', 'segundo_apellido', 'user_type', 'first_name', 'last_name', 'email', 'is_profiled')})

UserAdmin.fieldsets = tuple(fields)

admin.site.register(TME_002_User, UserAdmin)
admin.site.register(Víctima)
admin.site.register(Solicitante_Externo)
admin.site.register(Servidor_Público)

