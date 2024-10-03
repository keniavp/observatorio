from django.db import models

from Nomencladores.choises import comunidades_list, afiliacion_list, cobertura_list


class Comunidades(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    tipologia = models.CharField(choices=comunidades_list)
    afiliacion = models.CharField(choices=afiliacion_list)
    cobertura = models.CharField(choices=cobertura_list)
    categoria = models.CharField(max_length=500, verbose_name="Categoría", null=True, blank=True)
    tematica = models.CharField(max_length=500, verbose_name="Temática", null=True, blank=True)
    coordinador = models.CharField(max_length=500, verbose_name="Coordinador", null=True, blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente", null=True, blank=True)
    fecha = models.DateField(verbose_name="Fecha de Creación", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'comunidad'
        verbose_name_plural = 'comunidades'
        db_table = 'comunidad'
