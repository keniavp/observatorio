# Generated by Django 3.2.19 on 2023-10-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0002_conjuntodatos_documentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicadores',
            name='descripcion',
            field=models.CharField(max_length=250, verbose_name='Descripcion'),
        ),
    ]