# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('administrativo', 'Administrativo'), ('produccion', 'Produccion')], max_length=40)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('nivelPro', models.CharField(choices=[('tecnico', 'Tecnico'), ('tecnologo', 'Tecnologo'), ('profesional', 'Profesional'), ('maestria', 'Maestria'), ('doctorado', 'Doctorado')], max_length=100)),
                ('salario', models.IntegerField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='Avicola', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EventoGranja',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallina',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('edad', models.IntegerField(help_text='Ingrese la edad en dias')),
                ('raza', models.CharField(choices=[('black_rock', 'Black rock'), ('speckledy', 'Speckledy')], max_length=100)),
                ('fecha_nacimineto', models.DateField()),
                ('novedad', models.CharField(blank=True, max_length=100, null=True)),
                ('proceso', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Galpon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('tipo_zona', models.CharField(choices=[('productiva', 'Productiva'), ('levante', 'Levante')], max_length=30)),
                ('eventos', models.CharField(blank=True, max_length=100, null=True)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Granja',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cantGallinas', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Area')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidadGallinas', models.IntegerField()),
                ('fecha_nacimiento_gallinas', models.DateField()),
                ('galpon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Galpon')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('gallina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Gallina')),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('novedad', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('experiencia', models.IntegerField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Empleado')),
            ],
        ),
        migrations.AddField(
            model_name='vacuna',
            name='asistente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Veterinario'),
        ),
        migrations.AddField(
            model_name='vacuna',
            name='gallina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Gallina'),
        ),
        migrations.AddField(
            model_name='galpon',
            name='granja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Granja'),
        ),
        migrations.AddField(
            model_name='gallina',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Lote'),
        ),
        migrations.AddField(
            model_name='eventogranja',
            name='granja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Granja'),
        ),
        migrations.AddField(
            model_name='curso',
            name='veterinario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Veterinario'),
        ),
        migrations.AddField(
            model_name='area',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avicola.Empresa'),
        ),
    ]
