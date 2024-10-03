from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from Nomencladores.models import *


# Create your views here.
class HomeView(ListView):
    template_name = 'Dashboard.html'
    model = Pais

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Dashboard'
        context['year'] = datetime.today().year
        return context


class PaisesView(ListView):
    template_name = 'Gestion/Configuracion/Paises_list.html'
    model = Pais

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Paises'
        context['router'] = "paises"
        context['year'] = datetime.today().year
        return context


class ProvinciaView(ListView):
    template_name = 'Gestion/Configuracion/Provincia_list.html'
    model = Provincia

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Provincias'
        context['router'] = "provincia"
        context['year'] = datetime.today().year
        return context


class MunicipioView(ListView):
    template_name = 'Gestion/Configuracion/Municipio_list.html'
    model = Municipio

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Municipios'
        context['router'] = "municipio"
        context['year'] = datetime.today().year
        return context