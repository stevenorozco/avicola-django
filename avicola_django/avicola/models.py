from __future__ import unicode_literals

from django.db import models

RAZAS_GALLINAS = (
    ("black_rock" , "Black rock"),
    ("speckledy" , "Speckledy"),
)

TIPOS_AREAS = (
    ("administrativo" , "Administrativo"),
    ("produccion" , "Produccion"),
)

NIVELES_PROFESIONALES = (
    ("tecnico" , "Tecnico"),
    ("tecnologo" , "Tecnologo"),
    ("profesional" , "Profesional"),
    ("maestria" , "Maestria"),
    ("doctorado" , "Doctorado"),
)
# Create your models here.

class Empresa (models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, default="Avicola")

    def __unicode__(self):
        return self.nombre

class Area (models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=40, choices=TIPOS_AREAS)
    nombre = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return self.nombre

class Cargo (models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    area = models.ForeignKey(Area)

    def __unicode__(self):
        return self.nombre

class Empleado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tel = models.IntegerField(null=True, blank=True)
    cargo = models.ForeignKey(Cargo)
    nivelPro = models.CharField(max_length=100, choices=NIVELES_PROFESIONALES)
    salario = models.IntegerField()

    def __unicode__(self):
        return self.nombre

class Veterinario(models.Model):
    id = models.IntegerField(primary_key=True)
    experiencia = models.IntegerField()
    empleado = models.ForeignKey(Empleado)

    def __unicode__(self):
        return self.empleado.nombre

class Curso (models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    institucion =models.CharField(max_length=100)
    fecha = models.DateTimeField()
    veterinario = models.ForeignKey(Veterinario)

    def __unicode__(self):
        return self.nombre

class Granja(models.Model):
    id= models.IntegerField(primary_key=True)
    cantGallinas = models.IntegerField()
    area = models.ForeignKey(Area)

    def __unicode__(self):
        return str(self.id)

class Galpon(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.IntegerField()
    eventos = models.CharField(max_length=100, null=True, blank=True)
    capacidad = models.IntegerField()
    granja = models.ForeignKey(Granja)

    def __unicode__(self):
        return str(self.codigo)

class Lote(models.Model):
    id = models.IntegerField(primary_key=True)
    cantidadGallinas = models.IntegerField()
    galpon = models.ForeignKey(Galpon)

    def __unicode__(self):
        return str(self.id)

class Gallina(models.Model):
    id = models.IntegerField(primary_key=True)
    edad = models.IntegerField(help_text="Ingrese la edad en dias")
    raza = models.CharField(max_length=100, null=False, choices = RAZAS_GALLINAS)
    novedad  = models.CharField(max_length=100, null=True, blank=True)
    proceso  = models.CharField(max_length=100, null=True, blank=True)
    lote = models.ForeignKey(Lote)

    def __unicode__(self):
        return str(self.id)

class Tratamiento (models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    gallina = models.ForeignKey(Gallina)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return self.descripcion

class Vacuna (models.Model):
    id = models.IntegerField(primary_key=True)
    nombre =models.CharField(max_length=100)
    novedad = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField()
    asistente = models.ForeignKey(Veterinario)
    gallina = models.ForeignKey(Gallina)

    def __unicode__(self):
        return self.nombre


