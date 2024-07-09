from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
# admin.site.register(ConfigGolpe)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):    
    def Bandera(self, obj):
        return format_html('<img src="{}" width="50px" height="50px"/>'.format(obj.bandera))
    # resource_class = PaisResource
    list_display = ['id', 'nombre', 'sigla', 'Bandera']
    fieldsets = (
        ("general", {"fields": ("nombre","sigla",'bandera')}),        
    )
    list_filter = ("nombre","sigla")
    # Render filtered options only after 5 characters were entered
    filter_input_length = {
        "title": 5,
    }
    list_per_page = 10 
    
@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
     list_display = ['id', 'provincia', 'sigla']
    
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
     list_display = ['id', 'municipio', 'sigla']

@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ['id','ambito','nombre','categoria','imagen','entidad','pais','provincia','municipio','region','fuente','year','url','descriptor']

@admin.register(OrdenamientoJ)
class OrdenamientoJAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','tipologia','categoria','aprobado','entidad','url','year','pdf','concepto']
    
@admin.register(TratadosI)
class TratadosIAdmin(admin.ModelAdmin):
    list_display = ['id','tipologia','nombre','categoria','organismo','year','pdf','imagen','concepto']
    
        
# @admin.register(Datos)
# class DatosAdmin(admin.ModelAdmin):
#     list_display = ['id', 'dato','cjtodatos','titulo']
#     exclude=['ext']
    