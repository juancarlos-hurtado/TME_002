# Generated by Django 4.1.2 on 2022-12-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_delete_colonia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.CharField(blank=True, max_length=6, null=True)),
                ('colonia', models.CharField(blank=True, max_length=150, null=True)),
                ('delegación', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
