# Generated by Django 3.2.19 on 2023-10-31 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0005_auto_20231030_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicadores',
            name='descripcion',
        ),
    ]
