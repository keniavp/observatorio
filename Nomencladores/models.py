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


      
class Afiliacion(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Afiliación", help_text="Ingrese la afiliación")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la afiliación")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'afiliacion'
        verbose_name_plural = 'afiliaciones'
        db_table = 'afiliacion'
        
class Tipologia(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Tipologías", help_text="Ingrese la tipología")
    sigla = models.CharField(max_length=500, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la tipología")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'tipologia'
        verbose_name_plural = 'tipologias'
        db_table = 'tipologia'
        
class ComunidadesAcademicas(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Comunidad Académica", help_text="Ingrese la comunidad académica")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la comunidad académica")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'comunidad_academica'
        verbose_name_plural = 'comunidades_academicas'
        db_table = 'comunidad_academica'
        
class Cobertura(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Cobertura", help_text="Ingrese la cobertura")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la cobertura")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'cobertura'
        verbose_name_plural = 'coberturas'
        db_table = 'cobertura'
        
class Tematica(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Temática", help_text="Ingrese la temática")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la temática")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'tematica'
        verbose_name_plural = 'tematicas'
        db_table = 'tematica'
        
        
class Clasificacion(models.Model):
    clasif = models.CharField(max_length=500, verbose_name="Clasificación", help_text="Ingrese la clasificación")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la clasificación")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'clasificacion'
        verbose_name_plural = 'clasificaciones'
        db_table = 'clasificacion'
        
class Region(models.Model):
    region = models.CharField(max_length=500, verbose_name="Región", help_text="Ingrese la región")
    sigla = models.CharField(max_length=25, verbose_name="Sigla", null=True, blank=True,
                             help_text="Ingrese las siglas que identifican la región")
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'region'
        verbose_name_plural = 'regiones'
        db_table = 'region'


