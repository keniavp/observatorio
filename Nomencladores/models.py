from django.contrib.auth.models import User
from django.db import models

from Nomencladores.choises import *


class Pais(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="País", help_text="Ingrese el nombre del país.")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican el país.")
    bandera = models.URLField(null=True, blank=True, help_text="Ingrese la url donde se encuentra la bandera del país")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        db_table = 'pais'


class Provincia(models.Model):
    provincia = models.CharField(max_length=500, verbose_name="Provincia")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True)

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'
        db_table = 'provincia'


class Municipio(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    municipio = models.CharField(max_length=500, verbose_name="Municipio")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True)

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
        db_table = 'municipio'


class RecursosA(models.Model):
    programa = models.CharField(max_length=500, verbose_name="Programa", null=True, blank=True)
    titulo = models.CharField(max_length=500, verbose_name="Título", null=True, blank=True)
    capitulo = models.CharField(max_length=500, verbose_name="Capítulo/Número", null=True, blank=True)
    enlace = models.CharField(max_length=500, verbose_name="Enlace", null=True, blank=True)
    medio = models.CharField(max_length=500, verbose_name="Medio", null=True, blank=True)
    year = models.CharField(max_length=500, verbose_name="Año", null=True, blank=True)
    descriptores = models.CharField(max_length=500, verbose_name="Descriptores", null=True, blank=True)
    pais = models.CharField(max_length=500, verbose_name="País", null=True, blank=True)
    region = models.CharField(max_length=500, verbose_name="Región", null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'resurso'
        verbose_name_plural = 'recursos'
        db_table = 'recurso'
