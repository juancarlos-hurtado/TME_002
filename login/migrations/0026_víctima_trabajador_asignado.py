# Generated by Django 4.1.2 on 2023-01-03 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_víctima_coordinador_asignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='víctima',
            name='trabajador_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.trabajador_social'),
        ),
    ]
