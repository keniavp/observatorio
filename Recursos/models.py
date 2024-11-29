from django.db import models
from Nomencladores.choises import tipor_list
from Nomencladores.models import Clasificacion, Pais, Region, Tematica

# Create your models here.
class RecursosA(models.Model):
    tipo_recurso = models.CharField(choices=tipor_list)
    programa = models.CharField(max_length=500, verbose_name="Programa", null=True, blank=True)
    titulo = models.CharField(max_length=500, verbose_name="Título", null=True, blank=True)
    capitulo = models.CharField(max_length=500, verbose_name="Capítulo/Número", null=True, blank=True)
    enlace = models.CharField(max_length=500, verbose_name="Enlace", null=True, blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente", null=True, blank=True)
    medio = models.CharField(max_length=500, verbose_name="Medio", null=True, blank=True)
    year = models.CharField(max_length=500, verbose_name="Año", null=True, blank=True)
    descriptores = models.CharField(max_length=500, verbose_name="Descriptores", null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    tematica = models.ForeignKey(Tematica, on_delete=models.SET_NULL, null=True, blank=True)
    autores = models.CharField(max_length=1000, verbose_name="Autores", null=True, blank=True)
    editorial = models.CharField(max_length=1000, verbose_name="Editorial", null=True, blank=True)
    nombre_revista = models.CharField(max_length=1000, verbose_name="Nombre Revista", null=True, blank=True)
    no_edic = models.CharField(max_length=1000, verbose_name="Número de la edición", null=True, blank=True)
    resumen_art = models.CharField(max_length=10000, verbose_name="Resumen del artículo", null=True, blank=True)
    universidad = models.CharField(max_length=10000, verbose_name="Universidad", null=True, blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'resurso'
        verbose_name_plural = 'recursos'
        db_table = 'recurso'
