# Generated by Django 5.1.1 on 2024-11-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0003_alter_proyectos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='images/', verbose_name='Foto'),
        ),
    ]
