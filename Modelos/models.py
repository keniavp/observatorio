from http.client import SWITCHING_PROTOCOLS
from django.contrib.auth.models import User
from django.db import models
import os.path
from simple_history.models import HistoricalRecords
from observatorio import settings
from enum import Enum
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class Pais(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="País", help_text="Ingrese el nombre del país.")
    sigla = models.CharField(max_length=25, verbose_name="Sigla",null=True,blank=True,help_text="Ingrese las siglas que identifican el país.")
    bandera = models.URLField(null=True, blank=True,help_text="Ingrese la url donde se encuentra la bandera del país")
    
    def __str__(self):
            return self.nombre 
    
    
    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        db_table = 'pais'
        
class Provincia(models.Model):
        provincia = models.CharField(max_length=500, verbose_name="Provincia")
        sigla = models.CharField(max_length=25, verbose_name="Sigla",null=True,blank=True)
       
        def __str__(self):
                return self.provincia
        class Meta:
                verbose_name = 'provincia'
                verbose_name_plural = 'provincias'
                db_table = 'provincia'
                
class Municipio(models.Model):
        municipio = models.CharField(max_length=500, verbose_name="Municipio")
        sigla = models.CharField(max_length=25, verbose_name="Sigla",null=True,blank=True)
       
        def __str__(self):
                return self.provincia
        class Meta:
                verbose_name = 'municipio'
                verbose_name_plural = 'municipios'
                db_table = 'municipio'                


from django.db import models

class Proyectos(models.Model):
    class Ambito(models.TextChoices):
        NACIONAL = 1, 'Nacional'
        INTERNACIONAL = 2, 'Internacional'
                   
    ambito = models.IntegerField(choices=Ambito.choices)
    nombre = models.CharField(max_length=500, verbose_name="Nombre",null=True,blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría",null=True,blank=True)
    imagen = models.CharField(max_length=250, verbose_name="Foto",null=True, blank=True)
    entidad = models.CharField(max_length=500, verbose_name="Entidad Responsable",null=True,blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.CharField(max_length=500, verbose_name="Región",null=True,blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente",null=True,blank=True)
    year = models.CharField(max_length=500, verbose_name="Año",null=True,blank=True)
    url = models.CharField(max_length=500, verbose_name="URL",null=True,blank=True)
    descriptor = models.CharField(max_length=500, verbose_name="Descriptores",null=True,blank=True)
   
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        db_table = 'proyecto'
        
class OrdenamientoJ(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre",null=True,blank=True)
    tipologia = models.CharField(max_length=500, verbose_name="Tipología",null=True,blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría",null=True,blank=True)
    aprobado = models.CharField(max_length=500, verbose_name="Aprobado_por",null=True,blank=True)
    entidad = models.CharField(max_length=500, verbose_name="Entidad Responsable",null=True,blank=True)
    url = models.CharField(max_length=500, verbose_name="URL",null=True,blank=True)
    year = models.CharField(max_length=500, verbose_name="Fecha de emisión",null=True,blank=True)
    pdf = models.FileField(upload_to='media/documentos',null=True, blank=True)
    concepto = models.CharField(max_length=2000, verbose_name="Categoría Conceptual",null=True,blank=True)
   
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name = 'ordenamiento'
        verbose_name_plural = 'ordenamientos'
        db_table = 'ordenamiento'
        
class TratadosI(models.Model):
    class Tipologia(models.TextChoices):
        LEY = 1, 'Ley'
        DCL = 2, 'Decreto Ley'
        R = 3, 'Reglamento'             
        Res = 4 , 'Resolución'
        Acuerdo = 5 , 'Acuerdo'
        Norma =  6, 'Norma',
        Estatuto = 7 , 'Estatuto',
               
    tipologia = models.IntegerField(choices=Tipologia.choices)
    nombre = models.CharField(max_length=500, verbose_name="Nombre",null=True,blank=True)
    tipologia =  models.IntegerField(choices=Tipologia.choices)
    categoria = models.CharField(max_length=500, verbose_name="Categoría",null=True,blank=True)
    organismo = models.CharField(max_length=500, verbose_name="Organismo Internacional",null=True,blank=True)
    year = models.CharField(max_length=500, verbose_name="Fecha de emisión",null=True,blank=True)
    pdf = models.FileField(upload_to='media/documentos',null=True, blank=True)
    imagen = models.FileField(upload_to='media/images',null=True, blank=True)
    concepto = models.CharField(max_length=2000, verbose_name="Categoría Conceptual",null=True,blank=True)
   
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name = 'tratado'
        verbose_name_plural = 'tratados'
        db_table = 'tratado'
        
class EventosConv(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre",null=True,blank=True)
    imagen = models.FileField(upload_to='media/images',null=True, blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría",null=True,blank=True)
    entidad_responsable = models.CharField(max_length=500, verbose_name="Entidad Coord. o Responsable",null=True,blank=True)
    enlace = models.CharField(max_length=500, verbose_name="Enlace",null=True,blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente",null=True,blank=True)
    descriptores = models.CharField(max_length=500, verbose_name="Descriptores",null=True,blank=True)
   
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        db_table = 'evento'
        
class Comunidades(models.Model):
    class Tipologia(models.TextChoices):
        A = 1, 'Académica'
        C = 2, 'Científica'
        SC = 3, 'Sociedad civil'             
        ONG = 4 , 'ONG'
        Red = 5 , 'Red'
        O =  6, 'Otros',
    class Afiliacion(models.TextChoices):
        I = 1, 'Institucional'
        U = 2, 'Universidad'
        ONG = 3, 'ONG',                
    class Cobertura(models.TextChoices):
        P = 1, 'País'
        PROV = 2, 'Provincial'
        MUN = 3, 'Municipal'
        E = 4, 'Empresa'
        R = 5, 'Región',
    nombre = models.CharField(max_length=500, verbose_name="Nombre",null=True,blank=True)
    tipologia =  models.IntegerField(choices=Tipologia.choices)
    afiliacion =  models.IntegerField(choices=Afiliacion.choices)
    cobertura =  models.IntegerField(choices=Cobertura.choices)
    categoria = models.CharField(max_length=500, verbose_name="Categoría",null=True,blank=True)
    tematica = models.CharField(max_length=500, verbose_name="Temática",null=True,blank=True)
    coordinador = models.CharField(max_length=500, verbose_name="Coordinador",null=True,blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente",null=True,blank=True)
    fecha = models.DateField(verbose_name="Fecha de Creación",null=True,blank=True)
   
    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name = 'comunidad'
        verbose_name_plural = 'comunidades'
        db_table = 'comunidad'
        
class RecursosA(models.Model):
    programa = models.CharField(max_length=500, verbose_name="Programa",null=True,blank=True)
    titulo = models.CharField(max_length=500, verbose_name="Título",null=True,blank=True)
    capítulo = models.CharField(max_length=500, verbose_name="Capíyulo/Número",null=True,blank=True)
    enlace = models.CharField(max_length=500, verbose_name="Enlace",null=True,blank=True)
    medio = models.CharField(max_length=500, verbose_name="Medio",null=True,blank=True)
    year = models.CharField(max_length=500, verbose_name="Año",null=True,blank=True)
    descriptores = models.CharField(max_length=500, verbose_name="Descriptores",null=True,blank=True)
    pais = models.CharField(max_length=500, verbose_name="País",null=True,blank=True)
    region = models.CharField(max_length=500, verbose_name="Región",null=True,blank=True)

    def __str__(self):
            return self.titulo
    
    class Meta:
        verbose_name = 'resurso'
        verbose_name_plural = 'recursos'
        db_table = 'recurso'