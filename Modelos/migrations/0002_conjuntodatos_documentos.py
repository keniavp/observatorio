# Generated by Django 3.2.19 on 2023-10-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conjuntodatos',
            name='documentos',
            field=models.FileField(blank=True, null=True, upload_to='media/documentos'),
        ),
    ]
