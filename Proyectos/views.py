from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from Proyectos.forms import ProyectoForm
from Proyectos.models import Proyectos


# Create your views here.
class ProyectosView(ListView):
    template_name = 'Gestion/Proyectos/Proyectos_list.html'
    model = Proyectos

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Proyectos'
        context['router'] = "proyectos"
        context['year'] = datetime.today().year
        return context


class CrearProyectoView(CreateView):
    model = Proyectos
    form_class = ProyectoForm
    template_name = 'Gestion/Proyectos/Proyectos_new.html'
    success_url = reverse_lazy('proyectos')

    def post(self, request, *args, **kwargs):
        formulario = ProyectoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="proyectos")
        else:
            raise ValidationError("Error al crear el proyecto")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo proyecto'
        context['router'] = "Nuevo proyecto"
        context['year'] = datetime.today().year
        return context


class UpdateProyectoView(UpdateView):
    model = Proyectos
    form_class = ProyectoForm
    template_name = 'Gestion/Proyectos/Proyectos_update.html'
    success_url = reverse_lazy('proyectos')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar proyecto'
        context['router'] = "Actualizar proyecto"
        context['year'] = datetime.today().year
        return context


@login_required
def eliminar_proyecto(request, id):
    item = get_object_or_404(Proyectos, id=id)
    item.delete()
    return redirect(to="proyectos")