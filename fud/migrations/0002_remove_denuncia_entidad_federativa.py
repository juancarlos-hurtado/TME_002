# Generated by Django 4.1.2 on 2022-12-28 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denuncia',
            name='entidad_federativa',
        ),
    ]
