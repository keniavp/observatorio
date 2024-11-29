from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Comunidades.views import *
from Configuracion import settings
from Eventos.views import *
from Nomencladores.views import *
from Ordenamiento.views import *
from Proyectos.views import *
from Seguridad.views import LoginView, logout_view, UserListView
from Tratados.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    
    path('comunidades/', ComunidadesView.as_view(), name='comunidades'),
    path('nueva_comunidad/', CrearComunidadView.as_view(), name='nueva_comunidad'),
    path('actualizar_comunidad/<int:pk>/', UpdateComunidadView.as_view(), name='actualizar_comunidad'),
    path('eliminar_comunidad/<int:id>/', eliminar_comunidad, name='eliminar_comunidad'),

    path('paises/', PaisesView.as_view(), name='paises'),
     path('actualizar_pais/<int:pk>/', UpdatePaisView.as_view(), name='actualizar_pais'),
    path('eliminar_pais/<int:id>/', eliminar_pais, name='eliminar_pais'),
    path('nuevo_pais', CrearPaisView.as_view(), name='nuevo_pais'),
    
    path('municipios/', MunicipioView.as_view(), name='municipios'),
    path('actualizar_municipio/<int:pk>/', UpdateMunicipioView.as_view(), name='actualizar_municipio'),
    path('eliminar_municipios/<int:id>/', eliminar_municipios, name='eliminar_municipios'),
    path('nuevo_municipio', CrearMunicipioView.as_view(), name='nuevo_municipio'),
    
    path('provincias/', ProvinciaView.as_view(), name='provincias'),
    path('actualizar_provincia/<int:pk>/', UpdateProvinciaView.as_view(), name='actualizar_provincia'),
    path('eliminar_provincia/<int:id>/', eliminar_provincia, name='eliminar_provincia'),
    path('nueva_provincia', CrearProvinciaView.as_view(), name='nueva_provincia'),
    
    path('tipologias/', TipologiaView.as_view(), name='tipologias'),
    path('actualizar_tipologia/<int:pk>/', UpdateTipologiaView.as_view(), name='actualizar_tipologia'),
    path('eliminar_tipologia/<int:id>/', eliminar_tipologia, name='eliminar_tipologia'),
    path('nueva_tipologia', CrearTipologiaView.as_view(), name='nueva_tipologia'),
    
    path('coberturas/', CoberturaView.as_view(), name='coberturas'),
    path('actualizar_cobertura/<int:pk>/', UpdateCoberturaView.as_view(), name='actualizar_cobertura'),
    path('eliminar_cobertura/<int:id>/', eliminar_cobertura, name='eliminar_cobertura'),
    path('nueva_cobertura', CrearCoberturaView.as_view(), name='nueva_cobertura'),
    
    path('tematicas/', TematicaView.as_view(), name='tematicas'),
    path('actualizar_tematica/<int:pk>/', UpdateTematicaView.as_view(), name='actualizar_tematica'),
    path('eliminar_tematica/<int:id>/', eliminar_cobertura, name='eliminar_tematica'),
    path('nueva_tematica', CrearTematicaView.as_view(), name='nueva_tematica'),
    
    path('comunidades_academicas/', ComunidadesaView.as_view(), name='comunidades_academicas'),
    path('actualizar_comunidada/<int:pk>/', UpdateComunidadesaView.as_view(), name='actualizar_comunidada'),
    path('eliminar_comunidada/<int:id>/', eliminar_comunidada, name='eliminar_comunidada'),
    path('nueva_comunidada', CrearComunidadesaView.as_view(), name='nueva_comunidada'),
    
    path('clasificaciones/', ClasificacionesView.as_view(), name='clasificaciones'),
    path('actualizar_clasificacion/<int:pk>/', UpdateClasificacionesView.as_view(), name='actualizar_clasificacion'),
    path('eliminar_clasificacion/<int:id>/', eliminar_clasificacion, name='eliminar_clasificacion'),
    path('nueva_clasificacion', CrearClasificacionesView.as_view(), name='nueva_clasificacion'),
    
    path('afiliaciones/', AfiliacionesView.as_view(), name='afiliaciones'),
    path('actualizar_afiliacion/<int:pk>/', UpdateAfiliacionesView.as_view(), name='actualizar_afiliacion'),
    path('eliminar_afiliacion/<int:id>/', eliminar_afiliacion, name='eliminar_afiliacion'),
    path('nueva_afiliacion', CrearAfiliacionesView.as_view(), name='nueva_afiliacion'),
    
    path('regiones/', RegionesView.as_view(), name='regiones'),
    path('actualizar_region/<int:pk>/', UpdateRegionesView.as_view(), name='actualizar_region'),
    path('eliminar_region/<int:id>/', eliminar_region, name='eliminar_region'),
    path('nueva_region', CrearRegionesView.as_view(), name='nueva_region'),
    
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('nuevo_evento/', CrearEventoView.as_view(), name='nuevo_evento'),
    path('actualizar_evento/<int:pk>/', UpdateEventoView.as_view(), name='actualizar_evento'),
    path('eliminar_evento/<int:id>/', eliminar_evento, name='eliminar_evento'),

    path('ordenamiento/', OrdenamientoView.as_view(), name='ordenamiento'),
    path('nuevo_ordenamiento/', CrearOrdenamientoView.as_view(), name='nuevo_ordenamiento'),
    path('actualizar_ordenamiento/<int:pk>/', UpdateOrdenamientoView.as_view(), name='actualizar_ordenamientoo'),
    path('eliminar_ordenamiento/<int:id>/', eliminar_ordenamiento, name='eliminar_ordenamiento'),

    path('proyectos/', ProyectosView.as_view(), name='proyectos'),
    path('nuevo_proyecto/', CrearProyectoView.as_view(), name='nuevo_proyecto'),
    path('actualizar_proyecto/<int:pk>', UpdateProyectoView.as_view(), name='actualizar_proyecto'),
    path('eliminar_proyecto/<int:id>/', eliminar_proyecto, name='eliminar_proyecto'),

    path('tratados/', TratadoView.as_view(), name='tratados'),
    path('nuevo_tratado/', CrearTratadoView.as_view(), name='nuevo_tratado'),
    path('actualizar_tratado/<int:pk>/', UpdateTratadoView.as_view(), name='actualizar_tratado'),
    path('eliminar_tratado/<int:id>/', eliminar_tratado, name='eliminar_tratado'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('usuarios/', UserListView.as_view(), name='usuarios'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
