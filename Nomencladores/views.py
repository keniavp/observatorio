from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from Proyectos.models import *

from Nomencladores.models import *
from Nomencladores.forms import AfiliacionForm, ClasificacionForm, ComunidadaForm, MunicipioForm, PaisForm, ProvinciaForm, RegionForm,TipologiaForm,CoberturaForm, TematicaForm


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
        context['total_proyectos']=Proyectos.objects.all().count()
        context['year'] = datetime.today().year
        return context


class PaisesView(ListView):
    template_name = 'Gestion/Nomencladores/Paises_list.html'
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
    
class CrearPaisView(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'Gestion/Nomencladores/Pais_new.html'
    success_url = reverse_lazy('paises')

    def post(self, request, *args, **kwargs):
        formulario = PaisForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="paises")
        else:
            raise ValidationError("Error al crear el nuevo país")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo pais'
        context['router'] = "nuevo_pais"
        context['year'] = datetime.today().year
        return context
    
class UpdatePaisView(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'Gestion/Nomencladores/Pais_update.html'
    success_url = reverse_lazy('paises')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar pais'
        context['router'] = "actualizar_pais"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_pais(request, id):
    item = get_object_or_404(Pais, id=id)
    item.delete()
    return redirect(to="paises")
    


class ProvinciaView(ListView):
    template_name = 'Gestion/Nomencladores/Provincia_list.html'
    model = Provincia

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Provincias'
        context['router'] = "provincias"
        context['year'] = datetime.today().year
        return context

class CrearProvinciaView(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'Gestion/Nomencladores/Provincia_new.html'
    success_url = reverse_lazy('provincias')

    def post(self, request, *args, **kwargs):
        formulario = ProvinciaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="provincias")
        else:
            raise ValidationError("Error al crear la provincia")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva provincia'
        context['router'] = "nueva_provincia"
        context['year'] = datetime.today().year
        return context
    
class UpdateProvinciaView(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'Gestion/Nomencladores/Provincia_update.html'
    success_url = reverse_lazy('provincias')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar provincia'
        context['router'] = "actualizar_provincia"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_provincia(request, id):
    item = get_object_or_404(Provincia, id=id)
    item.delete()
    return redirect(to="provincias")
    
class MunicipioView(ListView):
    template_name = 'Gestion/Nomencladores/Municipio_list.html'
    model = Municipio

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Municipios'
        context['router'] = "municipios"
        context['year'] = datetime.today().year
        return context
    
class CrearMunicipioView(CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'Gestion/Nomencladores/Municipio_new.html'
    success_url = reverse_lazy('municipios')

    def post(self, request, *args, **kwargs):
        formulario = MunicipioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="municipios")
        else:
            raise ValidationError("Error al crear el municipio")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo municipio'
        context['router'] = "nuevo_municipio"
        context['year'] = datetime.today().year
        return context
    
class UpdateMunicipioView(UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'Gestion/Nomencladores/Municipio_update.html'
    success_url = reverse_lazy('municipios')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar municipio'
        context['router'] = "actualizar_municipio"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_municipios(request, id):
    item = get_object_or_404(Municipio, id=id)
    item.delete()
    return redirect(to="municipios")
    
class TipologiaView(ListView):
    template_name = 'Gestion/Nomencladores/Tipologia_list.html'
    model=Tipologia

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Tipologías"
        context['router'] = 'tipologias'
        context['year'] = datetime.today().year
        return context
    
class CrearTipologiaView(CreateView):
    model = Tipologia
    form_class = TipologiaForm
    template_name = 'Gestion/Nomencladores/Tipologia_new.html'
    success_url = reverse_lazy('tipologias')

    def post(self, request, *args, **kwargs):
        formulario = TipologiaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tipologias")
        else:
            raise ValidationError("Error al crear la nueva tipologia")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva tipologia'
        context['router'] = "nueva_tipologia"
        context['year'] = datetime.today().year
        return context
    
class UpdateTipologiaView(UpdateView):
    model = Tipologia
    form_class = TipologiaForm
    template_name = 'Gestion/Nomencladores/Tipologia_update.html'
    success_url = reverse_lazy('tipologias')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar tipologia'
        context['router'] = "actualizar_tipologia"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_tipologia(request, id):
    item = get_object_or_404(Tipologia, id=id)
    item.delete()
    return redirect(to="tipologias")



class CoberturaView(ListView):
    template_name = 'Gestion/Nomencladores/Cobertura_list.html'
    model=Cobertura

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Coberturas"
        context['router'] = 'coberturas'
        context['year'] = datetime.today().year
        return context
    
class CrearCoberturaView(CreateView):
    model = Cobertura
    form_class = CoberturaForm
    template_name = 'Gestion/Nomencladores/Cobertura_new.html'
    success_url = reverse_lazy('coberturas')

    def post(self, request, *args, **kwargs):
        formulario = CoberturaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="coberturas")
        else:
            raise ValidationError("Error al crear la nueva cobertura")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva cobertura'
        context['router'] = "nueva_cobertura"
        context['year'] = datetime.today().year
        return context
    
class UpdateCoberturaView(UpdateView):
    model = Cobertura
    form_class = CoberturaForm
    template_name = 'Gestion/Nomencladores/Cobertura_update.html'
    success_url = reverse_lazy('coberturas')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar cobertura'
        context['router'] = "actualizar_cobertura"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_cobertura(request, id):
    item = get_object_or_404(Cobertura, id=id)
    item.delete()
    return redirect(to="coberturas")


# desde aqui las tematicas

class TematicaView(ListView):
    template_name = 'Gestion/Nomencladores/Tematica_list.html'
    model=Tematica

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Tematicas"
        context['router'] = 'tematicas'
        context['year'] = datetime.today().year
        return context
    
class CrearTematicaView(CreateView):
    model = Tematica
    form_class = TematicaForm
    template_name = 'Gestion/Nomencladores/Tematica_new.html'
    success_url = reverse_lazy('tematicas')

    def post(self, request, *args, **kwargs):
        formulario = TematicaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tematicas")
        else:
            raise ValidationError("Error al crear la nueva tematica")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva temática'
        context['router'] = "nueva_tematica"
        context['year'] = datetime.today().year
        return context
    
class UpdateTematicaView(UpdateView):
    model = Tematica
    form_class = TematicaForm
    template_name = 'Gestion/Nomencladores/Tematica_update.html'
    success_url = reverse_lazy('tematicas')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar tematica'
        context['router'] = "actualizar_tematica"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_tematica(request, id):
    item = get_object_or_404(Tematica, id=id)
    item.delete()
    return redirect(to="tematicas")


# desde aqui las comnidades_academicas

class ComunidadesaView(ListView):
    template_name = 'Gestion/Nomencladores/ComunidadesA_list.html'
    model=ComunidadesAcademicas

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Comunidades"
        context['router'] = 'comunidades_academicas'
        context['year'] = datetime.today().year
        return context
    
class CrearComunidadesaView(CreateView):
    model = ComunidadesAcademicas
    form_class = ComunidadaForm
    template_name = 'Gestion/Nomencladores/ComunidadesA_new.html'
    success_url = reverse_lazy('comunidades_academicas')

    def post(self, request, *args, **kwargs):
        formulario = ComunidadaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="comunidades_academicas")
        else:
            raise ValidationError("Error al crear la nueva comunidad")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva comunidad'
        context['router'] = "nueva_comunidada"
        context['year'] = datetime.today().year
        return context
    
class UpdateComunidadesaView(UpdateView):
    model = ComunidadesAcademicas
    form_class = ComunidadaForm
    template_name = 'Gestion/Nomencladores/ComunidadesA_update.html'
    success_url = reverse_lazy('comunidades_academicas')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar comunidad'
        context['router'] = "actualizar_comunidada"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_comunidada(request, id):
    item = get_object_or_404(ComunidadesAcademicas, id=id)
    item.delete()
    return redirect(to="comunidades_academicas")

# desde aqui las afiliaciones

class AfiliacionesView(ListView):
    template_name = 'Gestion/Nomencladores/Afiliacion_list.html'
    model=Afiliacion

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Afiliaciones"
        context['router'] = 'afiliaciones'
        context['year'] = datetime.today().year
        return context
    
class CrearAfiliacionesView(CreateView):
    model = Afiliacion
    form_class = AfiliacionForm
    template_name = 'Gestion/Nomencladores/Afiliacion_new.html'
    success_url = reverse_lazy('afiliaciones')

    def post(self, request, *args, **kwargs):
        formulario = AfiliacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="afiliaciones")
        else:
            raise ValidationError("Error al crear la nueva afiliación")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva afiliación'
        context['router'] = "nueva_afiliacion"
        context['year'] = datetime.today().year
        return context
    
class UpdateAfiliacionesView(UpdateView):
    model = Afiliacion
    form_class = AfiliacionForm
    template_name = 'Gestion/Nomencladores/Afiliacion_update.html'
    success_url = reverse_lazy('afiliaciones')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar afiliación'
        context['router'] = "actualizar_afiliacion"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_afiliacion(request, id):
    item = get_object_or_404(Afiliacion, id=id)
    item.delete()
    return redirect(to="afiliaciones")


#desde aqui las clasificaciones

class ClasificacionesView(ListView):
    template_name = 'Gestion/Nomencladores/Clasificacion_list.html'
    model=Clasificacion

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Clasificación"
        context['router'] = 'clasificaciones'
        context['year'] = datetime.today().year
        return context
    
class CrearClasificacionesView(CreateView):
    model = Clasificacion
    form_class = ClasificacionForm
    template_name = 'Gestion/Nomencladores/Clasificacion_new.html'
    success_url = reverse_lazy('clasificaciones')

    def post(self, request, *args, **kwargs):
        formulario = ClasificacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="clasificaciones")
        else:
            raise ValidationError("Error al crear la nueva clasificación")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva clasificacion'
        context['router'] = "nueva_clasificacion"
        context['year'] = datetime.today().year
        return context
    
class UpdateClasificacionesView(UpdateView):
    model = Clasificacion
    form_class = ClasificacionForm
    template_name = 'Gestion/Nomencladores/Clasificacion_update.html'
    success_url = reverse_lazy('clasificaciones')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar clasificacion'
        context['router'] = "actualizar_clasificacion"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_clasificacion(request, id):
    item = get_object_or_404(Clasificacion, id=id)
    item.delete()
    return redirect(to="clasificaciones")

#desde aqui las regiones

class RegionesView(ListView):
    template_name = 'Gestion/Nomencladores/Region_list.html'
    model=Region

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Región"
        context['router'] = 'regiones'
        context['year'] = datetime.today().year
        return context
    
class CrearRegionesView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'Gestion/Nomencladores/Region_new.html'
    success_url = reverse_lazy('regiones')

    def post(self, request, *args, **kwargs):
        formulario = RegionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="regiones")
        else:
            raise ValidationError("Error al crear la nueva región")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nueva region'
        context['router'] = "nueva_region"
        context['year'] = datetime.today().year
        return context
    
class UpdateRegionesView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'Gestion/Nomencladores/Region_update.html'
    success_url = reverse_lazy('regiones')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        pk = self.kwargs.get('pk')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar region'
        context['router'] = "actualizar_region"
        context['year'] = datetime.today().year
        return context

@login_required
def eliminar_region(request, id):
    item = get_object_or_404(Region, id=id)
    item.delete()
    return redirect(to="regiones")
    