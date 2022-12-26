# Generated by Django 4.1.2 on 2022-12-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_colonia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colonia',
            old_name='nombre',
            new_name='colonia',
        ),
        migrations.AddField(
            model_name='colonia',
            name='estado',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]