from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from Eventos.forms import EventosForm
from Eventos.models import EventosConv


# Create your views here.
class EventosView(ListView):
    template_name = 'Gestion/Eventos/Eventos_list.html'
    model = EventosConv

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eventos'
        context['router'] = "eventos"
        context['year'] = datetime.today().year
        return context


class CrearEventoView(CreateView):
    model = EventosConv
    form_class = EventosForm
    template_name = 'Gestion/Eventos/Eventos_new.html'
    success_url = reverse_lazy('eventos')

    def post(self, request, *args, **kwargs):
        formulario = EventosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="eventos")
        else:
            raise ValidationError("Error al crear el evento")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo evento'
        context['router'] = "Nuevo evento"
        context['year'] = datetime.today().year
        return context


class UpdateEventoView(UpdateView):
    model = EventosConv
    form_class = EventosForm
    template_name = 'Gestion/Eventos/Eventos_update.html'
    success_url = '/eventos/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar evento'
        context['router'] = "Actualizar evento"
        context['year'] = datetime.today().year
        return context


@login_required
def eliminar_evento(request, id):
    item = get_object_or_404(EventosConv, id=id)
    item.delete()
    return redirect(to="eventos")
