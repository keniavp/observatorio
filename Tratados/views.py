from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from Tratados.forms import TratadoForm
from Tratados.models import TratadosI


# Create your views here.
class TratadoView(ListView):
    template_name = 'Gestion/Tratados/Tratados_list.html'
    model = TratadosI

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Tratados'
        context['router'] = "tratados"
        context['year'] = datetime.today().year
        return context


class CrearTratadoView(CreateView):
    model = TratadosI
    form_class = TratadoForm
    template_name = 'Gestion/Tratados/Tratados_new.html'
    success_url = reverse_lazy('tratados')

    def post(self, request, *args, **kwargs):
        formulario = TratadoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tratados")
        else:
            raise ValidationError("Error al crear el tratado")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo tratado'
        context['router'] = "Nuevo tratado"
        context['year'] = datetime.today().year
        return context


class UpdateTratadoView(UpdateView):
    model = TratadosI
    form_class = TratadoForm
    template_name = 'Gestion/Tratados/Tratados_update.html'
    success_url = '/tratados/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar tratados'
        context['router'] = "Actualizar tratados"
        context['year'] = datetime.today().year
        return context


@login_required
def eliminar_tratado(request, id):
    item = get_object_or_404(TratadosI, id=id)
    item.delete()
    return redirect(to="tratados")