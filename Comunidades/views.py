from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from Comunidades.form import ComunidadesForm
from Comunidades.models import Comunidades


# Create your views here.
class ComunidadesView(ListView):
    template_name = 'Gestion/Comunidades/Comunidades_list.html'
    model = Comunidades

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Comunidades'
        context['router'] = "comunidades"
        context['year'] = datetime.today().year
        return context


class CrearComunidadView(CreateView):
    model = Comunidades
    form_class = ComunidadesForm
    template_name = 'Gestion/Comunidades/Comunidades_new.html'
    success_url = '/comunidades/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva comunidad'
        context['router'] = "Nueva comunidad"
        context['year'] = datetime.today().year
        return context


class UpdateComunidadView(UpdateView):
    model = Comunidades
    form_class = ComunidadesForm
    template_name = 'Gestion/Comunidades/Comunidades_update.html'
    success_url = '/comunidades/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar comunidad'
        context['router'] = "Actualizar comunidad"
        context['year'] = datetime.today().year
        return context


@login_required
def eliminar_comunidad(request, id):
    item = get_object_or_404(Comunidades, id=id)
    item.delete()
    return redirect(to="comunidades")
