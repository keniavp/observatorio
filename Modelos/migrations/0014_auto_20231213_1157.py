# Generated by Django 3.2.19 on 2023-12-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0013_auto_20231125_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='ext',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name=' EXT'),
        ),
        migrations.AddField(
            model_name='datos',
            name='titulo',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Título'),
        ),
    ]
