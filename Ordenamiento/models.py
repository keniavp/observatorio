from django.db import models
from Nomencladores.models import Tematica,Tipologia



# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    concepto = models.CharField(max_length=2000, verbose_name="Concepto", null=True, blank=True)
    def __str__(self):
        return self.nombre

class OrdenamientoJ(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE,blank=True,null=True)
    aprobado = models.CharField(max_length=500, verbose_name="Aprobado_por", null=True, blank=True)
    entidad = models.CharField(max_length=500, verbose_name="Entidad Responsable", null=True, blank=True)
    url = models.CharField(max_length=500, verbose_name="URL", null=True, blank=True)
    year = models.CharField(max_length=500, verbose_name="Fecha de emisión", null=True, blank=True)
    pdf = models.FileField(upload_to='media/documentos', null=True, blank=True)
    articulos = models.ManyToManyField(Articulo, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'ordenamiento'
        verbose_name_plural = 'ordenamientos'
        db_table = 'ordenamiento'