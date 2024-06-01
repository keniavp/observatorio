from http.client import SWITCHING_PROTOCOLS
from django.contrib.auth.models import User
from django.db import models
import os.path
from simple_history.models import HistoricalRecords

from observatorio import settings


class Pais(models.Model):
    nombre = models.CharField(max_length=25, verbose_name="País")
    sigla = models.CharField(max_length=115, verbose_name="Sigla",null=True,blank=True)
    bandera = models.CharField(max_length=250, verbose_name="Bandera",null=True, blank=True)    

    def __str__(self):
            return self.nombre
    
    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        db_table = 'pais'


# class Publicadores(models.Model):
#     imagen = models.FileField(upload_to='media/publicadores',null=True, blank=True)
#     nombre = models.CharField(max_length=250, verbose_name="nombre",null=True, blank=True)
#     descripcion = models.CharField(max_length=250, verbose_name="descripcion",null=True, blank=True)
#     face = models.CharField(max_length=250, verbose_name="face",null=True, blank=True)
#     phone = models.TextField(verbose_name="telefono",null=True, blank=True)
#     web = models.TextField(verbose_name="web",null=True, blank=True)
    
#     def __str__(self):
#             return self.nombre
    
       
#     class Meta:
#         verbose_name = 'publicador'
#         verbose_name_plural = 'publicadores'
#         db_table = 'publicador'


# class ConjuntoDatos(models.Model):
#     categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
#     publicadores = models.ManyToManyField(Publicadores)
#     descripcion = models.CharField(max_length=250, verbose_name="descripcion",null=True, blank=True)
#     titulo = models.CharField(max_length=250, verbose_name="titulo",null=True, blank=True) 
#     history = HistoricalRecords(user_related_name='historial_de_cjtodatos')    
    
#     def __str__(self):
#             return self.titulo 
    

#     class Meta:
#         verbose_name = 'conjunto_dato'
#         verbose_name_plural = 'conjunto_datos'
#         db_table = 'conjunto_dato'
        
# class Proyectos(models.Model):
#    descripcion = models.TextField(verbose_name="Descripción")
#    titulo = models.CharField(max_length=250, verbose_name="Título")
#    icon_text = models.CharField(max_length=250, verbose_name="Imagen")
   
#    def __str__(self):
#             return self.titulo
   
#    class Meta:
#         verbose_name = 'proyecto'
#         verbose_name_plural = 'proyectos'
#         db_table = 'proyecto'

# class Datos(models.Model):
#     titulo = models.CharField(max_length=250, verbose_name="Título",null=True,blank=True)
#     ext = models.CharField(max_length=250, verbose_name=" EXT",null=True,blank=True)
#     dato = models.FileField(upload_to='media/documentos',null=True, blank=True)
#     cjtodatos = models.ForeignKey(ConjuntoDatos, on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = 'dato'
#         verbose_name_plural = 'datos'
#         db_table = 'dato' 
        
#     def __str__(self):
#             return self.titulo
    
#     def save(self, *args, **kwargs):
#         if not self.ext:
#             filename = self.dato.name
#             ext = os.path.splitext(filename)[1][1:]
#             if ext == 'pdf':
#                 self.ext = '&#xf1c1;'
#             elif ext == 'csv':
#                 self.ext = '&#xf1c3;'
#             else:
#                 self.ext ='&#xf016;'
             
#         # self.ext = ext
#         super(Datos, self).save(*args, **kwargs) 
        
        