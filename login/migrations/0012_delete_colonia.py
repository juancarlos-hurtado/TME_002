# Generated by Django 4.1.2 on 2022-12-26 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_rename_nombre_colonia_colonia_colonia_estado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Colonia',
        ),
    ]