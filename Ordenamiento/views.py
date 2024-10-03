from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from Ordenamiento.forms import OrdenamientoForm
from Ordenamiento.models import OrdenamientoJ


# Create your views here.
class OrdenamientoView(ListView):
    template_name = 'Gestion/Ordenamiento/Ordenamiento_list.html'
    model = OrdenamientoJ

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ordenamiento'
        context['router'] = "ordenamiento"
        context['year'] = datetime.today().year
        return context


class CrearOrdenamientoView(CreateView):
    model = OrdenamientoJ
    form_class = OrdenamientoForm
    template_name = 'Gestion/Ordenamiento/Ordenamiento_new.html'
    success_url = reverse_lazy('ordenamiento')

    def post(self, request, *args, **kwargs):
        formulario = OrdenamientoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ordenamiento")
        else:
            raise ValidationError("Error al crear el ordenamiento")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo ordenamiento'
        context['router'] = "Nuevo ordenamiento"
        context['year'] = datetime.today().year
        return context


class UpdateOrdenamientoView(UpdateView):
    model = OrdenamientoJ
    form_class = OrdenamientoForm
    template_name = 'Gestion/Ordenamiento/Ordenamiento_update.html'
    success_url = '/ordenamiento/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar ordenamiento'
        context['router'] = "Actualizar ordenamiento"
        context['year'] = datetime.today().year
        return context


@login_required
def eliminar_ordenamiento(request, id):
    item = get_object_or_404(OrdenamientoJ, id=id)
    item.delete()
    return redirect(to="ordenamiento")
