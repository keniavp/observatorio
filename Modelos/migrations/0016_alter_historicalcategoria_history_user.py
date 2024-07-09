# Generated by Django 3.2.19 on 2023-12-27 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Modelos', '0015_historicalcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalcategoria',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historial_de_categoria', to=settings.AUTH_USER_MODEL),
        ),
    ]
