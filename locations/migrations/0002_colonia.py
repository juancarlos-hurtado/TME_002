# Generated by Django 4.1.2 on 2022-12-29 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.CharField(blank=True, max_length=6, null=True)),
                ('colonia', models.CharField(blank=True, max_length=150, null=True)),
                ('alcaldia', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]