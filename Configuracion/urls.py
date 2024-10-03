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
    path('municipios/', MunicipioView.as_view(), name='municipios'),
    path('provincias/', ProvinciaView.as_view(), name='provincias'),

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
    path('actualizar_proyecto/', UpdateProyectoView.as_view(), name='actualizar_proyecto'),
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
