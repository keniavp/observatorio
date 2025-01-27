from django.contrib import admin

from Comunidades.models import Comunidades
from Eventos.models import EventosConv
from Ordenamiento.models import OrdenamientoJ
from Proyectos.models import Proyectos
from Tratados.models import TratadosI
from .models import *
from django.utils.html import format_html

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    def Bandera(self, obj):
        return format_html('<img src="{}" width="50px" height="50px"/>'.format(obj.bandera))

    # resource_class = PaisResource
    list_display = ['id', 'nombre', 'sigla', 'Bandera']
    fieldsets = (
        ("general", {"fields": ("nombre", "sigla", 'bandera')}),
    )
    list_filter = ("nombre", "sigla")
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


@admin.register(EventosConv)
class EventosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'imagen']


@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ['id', 'ambito', 'nombre', 'categoria', 'imagen', 'entidad', 'pais', 'provincia', 'municipio',
                    'region', 'fuente', 'year', 'url', 'descriptor']


@admin.register(OrdenamientoJ)
class OrdenamientoJAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'tipologia', 'aprobado', 'entidad', 'url', 'year', 'pdf']


@admin.register(TratadosI)
class TratadosIAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipologia', 'nombre', 'categoria', 'organismo', 'year', 'pdf', 'imagen', 'concepto']



admin.site.register(Comunidades)
