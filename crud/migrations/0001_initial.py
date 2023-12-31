# Generated by Django 4.2.1 on 2023-06-27 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['marca'],
            },
        ),
        migrations.CreateModel(
            name='Joyeria',
            fields=[
                ('idJoyeria', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo de Joya')),
                ('value', models.IntegerField(verbose_name='Valor')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('image', models.ImageField(blank=True, null=True, upload_to='joyeria', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.marca', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'joyeria',
                'verbose_name_plural': 'joyerias',
                'ordering': ['name', 'idJoyeria'],
            },
        ),
    ]
