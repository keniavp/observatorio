from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(ConfigGolpe)

@admin.register(Pais)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'sigla', 'bandera']
    
    
        
# @admin.register(Datos)
# class DatosAdmin(admin.ModelAdmin):
#     list_display = ['id', 'dato','cjtodatos','titulo']
#     exclude=['ext']
    