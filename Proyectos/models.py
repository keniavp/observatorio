from django.db import models

from Nomencladores.choises import ambito_list
from Nomencladores.models import Pais, Provincia, Municipio


# Create your models here.
class Proyectos(models.Model):
    ambito = models.CharField(choices=ambito_list)
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría", null=True, blank=True)
    imagen = models.FileField(upload_to='media/images', null=True, blank=True)
    entidad = models.CharField(max_length=500, verbose_name="Entidad Responsable", null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.CharField(max_length=500, verbose_name="Región", null=True, blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente", null=True, blank=True)
    year = models.CharField(max_length=500, verbose_name="Año", null=True, blank=True)
    url = models.CharField(max_length=500, verbose_name="URL", null=True, blank=True)
    descriptor = models.CharField(max_length=2000, verbose_name="Descriptores", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        db_table = 'proyecto'