# Generated by Django 3.2.19 on 2024-06-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0028_remove_pais_bandera_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='bandera',
            field=models.URLField(blank=True, help_text='Ingrese la url donde se encuentra la bandera del país', null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(help_text='Ingrese el nombre del país.', max_length=500, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='sigla',
            field=models.CharField(blank=True, help_text='Ingrese las siglas que identifican el país.', max_length=25, null=True, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='ambito',
            field=models.IntegerField(choices=[('1', 'Nacional'), ('2', 'Internacional')]),
        ),
        migrations.AlterField(
            model_name='tratadosi',
            name='tipologia',
            field=models.IntegerField(choices=[('1', 'Ley'), ('2', 'Decreto Ley'), ('3', 'Reglamento'), ('4', 'Resolución'), ('5', 'Acuerdo'), ('6', 'Norma'), ('7', 'Estatuto')]),
        ),
    ]
