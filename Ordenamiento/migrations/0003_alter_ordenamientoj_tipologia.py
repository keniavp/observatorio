# Generated by Django 5.1.1 on 2024-11-14 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomencladores', '0002_afiliacion_cobertura_comunidadesacademicas_tematica_and_more'),
        ('Ordenamiento', '0002_remove_ordenamientoj_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenamientoj',
            name='tipologia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Nomencladores.tipologia'),
        ),
    ]