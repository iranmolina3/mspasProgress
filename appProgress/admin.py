from django.contrib import admin
from .models import *


# Register your models here.

class AdminPersona(admin.ModelAdmin):
    search_fields = ['primer_nombre']
    list_display = ['pk_persona', 'primer_nombre', 'primer_apellido', 'cui', 'estado']

admin.site.register(tbl_persona, AdminPersona)

class AdminUsuario(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['pk_usuario', 'usuario', 'estado']

admin.site.register(tbl_usuario, AdminUsuario)