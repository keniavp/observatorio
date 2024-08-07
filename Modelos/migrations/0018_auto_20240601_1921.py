# Generated by Django 3.2.19 on 2024-06-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0017_historicalconjuntodatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='País')),
                ('sigla', models.CharField(blank=True, max_length=115, null=True, verbose_name='Sigla')),
                ('bandera', models.CharField(blank=True, max_length=250, null=True, verbose_name='Bandera')),
            ],
            options={
                'verbose_name': 'pais',
                'verbose_name_plural': 'paises',
                'db_table': 'pais',
            },
        ),
        migrations.RemoveField(
            model_name='conjuntodatos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='conjuntodatos',
            name='publicadores',
        ),
        migrations.RemoveField(
            model_name='datos',
            name='cjtodatos',
        ),
        migrations.RemoveField(
            model_name='historicalcategoria',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalconjuntodatos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='historicalconjuntodatos',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='Proyectos',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='ConjuntoDatos',
        ),
        migrations.DeleteModel(
            name='Datos',
        ),
        migrations.DeleteModel(
            name='HistoricalCategoria',
        ),
        migrations.DeleteModel(
            name='HistoricalConjuntoDatos',
        ),
        migrations.DeleteModel(
            name='Publicadores',
        ),
    ]
