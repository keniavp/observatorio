# Generated by Django 5.1.1 on 2024-12-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0002_alter_eventosconv_descriptores'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventosconv',
            name='fechaf',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Fin'),
        ),
        migrations.AddField(
            model_name='eventosconv',
            name='fechai',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio'),
        ),
    ]
