# Generated by Django 4.1.2 on 2023-01-03 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_alter_víctima_colonia_alter_víctima_del_mun'),
    ]

    operations = [
        migrations.AddField(
            model_name='víctima',
            name='coordinador_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.coordinador'),
        ),
    ]
