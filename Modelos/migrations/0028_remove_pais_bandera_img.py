# Generated by Django 3.2.19 on 2024-06-05 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0027_auto_20240603_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='bandera_img',
        ),
    ]
