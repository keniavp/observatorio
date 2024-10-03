from django.db import models

# Create your models here.
class EventosConv(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    imagen = models.FileField(upload_to='media/images', null=True, blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría", null=True, blank=True)
    entidad_responsable = models.CharField(max_length=500, verbose_name="Entidad Coord. o Responsable", null=True,
                                           blank=True)
    enlace = models.CharField(max_length=500, verbose_name="Enlace", null=True, blank=True)
    fuente = models.CharField(max_length=500, verbose_name="Fuente", null=True, blank=True)
    descriptores = models.CharField(max_length=500, verbose_name="Descriptores", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        db_table = 'evento'
