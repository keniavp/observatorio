from django.db import models

# Create your models here.
class OrdenamientoJ(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre", null=True, blank=True)
    tipologia = models.CharField(max_length=500, verbose_name="Tipología", null=True, blank=True)
    categoria = models.CharField(max_length=500, verbose_name="Categoría", null=True, blank=True)
    aprobado = models.CharField(max_length=500, verbose_name="Aprobado_por", null=True, blank=True)
    entidad = models.CharField(max_length=500, verbose_name="Entidad Responsable", null=True, blank=True)
    url = models.CharField(max_length=500, verbose_name="URL", null=True, blank=True)
    year = models.CharField(max_length=500, verbose_name="Fecha de emisión", null=True, blank=True)
    pdf = models.FileField(upload_to='media/documentos', null=True, blank=True)
    concepto = models.CharField(max_length=2000, verbose_name="Categoría Conceptual", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'ordenamiento'
        verbose_name_plural = 'ordenamientos'
        db_table = 'ordenamiento'