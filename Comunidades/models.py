from django.db import models

from Nomencladores.models import ComunidadesAcademicas, Afiliacion, Cobertura


class Comunidades(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    comunid = models.ForeignKey(ComunidadesAcademicas, on_delete=models.CASCADE,null=True, blank=True)
    afiliacion = models.ForeignKey(Afiliacion, on_delete=models.CASCADE)
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=500, verbose_name="Categoría", null=True, blank=True)
    tematica = models.CharField(max_length=500, verbose_name="Temática", null=True, blank=True)
    coordinador = models.CharField(max_length=500, verbose_name="Coordinador", null=True, blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Enlace", null=True, blank=True)
    fecha = models.DateField(verbose_name="Fecha de Creación", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'comunidad'
        verbose_name_plural = 'comunidades'
        db_table = 'comunidad'
