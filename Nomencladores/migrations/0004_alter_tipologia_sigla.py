# Generated by Django 5.1.1 on 2024-11-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomencladores', '0003_alter_tipologia_nombre_alter_tipologia_sigla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologia',
            name='sigla',
            field=models.CharField(blank=True, help_text='Ingrese las siglas que identifican la tipología', max_length=500, null=True, verbose_name='Sigla'),
        ),
    ]
