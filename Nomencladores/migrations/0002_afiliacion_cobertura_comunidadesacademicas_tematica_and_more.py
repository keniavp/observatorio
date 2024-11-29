# Generated by Django 5.1.1 on 2024-11-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese la afiliación', max_length=500, verbose_name='Afiliación')),
                ('sigla', models.CharField(blank=True, help_text='Ingrese las siglas que identifican la afiliación', max_length=25, null=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'afiliacion',
                'verbose_name_plural': 'afiliaciones',
                'db_table': 'afiliacion',
            },
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese la cobertura', max_length=500, verbose_name='Cobertura')),
                ('sigla', models.CharField(blank=True, help_text='Ingrese las siglas que identifican la cobertura', max_length=25, null=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'cobertura',
                'verbose_name_plural': 'coberturas',
                'db_table': 'cobertura',
            },
        ),
        migrations.CreateModel(
            name='ComunidadesAcademicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese la comunidad académica', max_length=500, verbose_name='Comunidad Académica')),
                ('sigla', models.CharField(blank=True, help_text='Ingrese las siglas que identifican la comunidad académica', max_length=25, null=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'comunidad_academica',
                'verbose_name_plural': 'comunidades_academicas',
                'db_table': 'comunidad_academica',
            },
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese la temática', max_length=500, verbose_name='Temática')),
                ('sigla', models.CharField(blank=True, help_text='Ingrese las siglas que identifican la temática', max_length=25, null=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'tematica',
                'verbose_name_plural': 'tematicas',
                'db_table': 'tematica',
            },
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese la tipologia', max_length=500, verbose_name='Tipologias')),
                ('sigla', models.CharField(blank=True, help_text='Ingrese las siglas que identifican la tipologia', max_length=25, null=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'tipologia',
                'verbose_name_plural': 'tipologias',
                'db_table': 'tipologia',
            },
        ),
        migrations.AlterField(
            model_name='recursosa',
            name='capitulo',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Capítulo/Número'),
        ),
    ]