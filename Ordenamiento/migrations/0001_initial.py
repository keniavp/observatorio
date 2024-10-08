# Generated by Django 5.1.1 on 2024-10-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenamientoJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nombre')),
                ('tipologia', models.CharField(blank=True, max_length=500, null=True, verbose_name='Tipología')),
                ('categoria', models.CharField(blank=True, max_length=500, null=True, verbose_name='Categoría')),
                ('aprobado', models.CharField(blank=True, max_length=500, null=True, verbose_name='Aprobado_por')),
                ('entidad', models.CharField(blank=True, max_length=500, null=True, verbose_name='Entidad Responsable')),
                ('url', models.CharField(blank=True, max_length=500, null=True, verbose_name='URL')),
                ('year', models.CharField(blank=True, max_length=500, null=True, verbose_name='Fecha de emisión')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/documentos')),
                ('concepto', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Categoría Conceptual')),
            ],
            options={
                'verbose_name': 'ordenamiento',
                'verbose_name_plural': 'ordenamientos',
                'db_table': 'ordenamiento',
            },
        ),
    ]
