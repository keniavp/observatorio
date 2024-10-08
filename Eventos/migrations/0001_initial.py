# Generated by Django 5.1.1 on 2024-10-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventosConv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nombre')),
                ('imagen', models.FileField(blank=True, null=True, upload_to='media/images')),
                ('categoria', models.CharField(blank=True, max_length=500, null=True, verbose_name='Categoría')),
                ('entidad_responsable', models.CharField(blank=True, max_length=500, null=True, verbose_name='Entidad Coord. o Responsable')),
                ('enlace', models.CharField(blank=True, max_length=500, null=True, verbose_name='Enlace')),
                ('fuente', models.CharField(blank=True, max_length=500, null=True, verbose_name='Fuente')),
                ('descriptores', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descriptores')),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
                'db_table': 'evento',
            },
        ),
    ]
