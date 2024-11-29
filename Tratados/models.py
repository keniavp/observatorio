from django.db import models


from Nomencladores.models import Tipologia


# Create your models here.
class TratadosI(models.Model):
    tipologia = models.ForeignKey(Tipologia, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría", null=True, blank=True)
    organismo = models.CharField(max_length=500, verbose_name="Organismo Internacional", null=True, blank=True)
    year = models.CharField(max_length=500, verbose_name="Fecha de emisión", null=True, blank=True)
    pdf = models.FileField(upload_to='media/documentos', null=True, blank=True)
    imagen = models.FileField(upload_to='media/images', null=True, blank=True)
    concepto = models.CharField(max_length=2000, verbose_name="Categoría Conceptual", null=True, blank=True)
    enlace = models.CharField(max_length=1000, verbose_name="Enlace", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'tratado'
        verbose_name_plural = 'tratados'
        db_table = 'tratado'