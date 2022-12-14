# Generated by Django 4.1.2 on 2023-01-03 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0028_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='víctima',
            name='medico_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.medico'),
        ),
        migrations.AddField(
            model_name='víctima',
            name='psicologo_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.psicologo'),
        ),
    ]
