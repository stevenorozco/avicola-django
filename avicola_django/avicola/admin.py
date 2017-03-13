from django.contrib import admin
from .models import *

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    fields = ("nombre",)

class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo", "nombre", "empresa")
    fields = ( "tipo", "nombre", "empresa")

class CargoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "area")
    fields = ("nombre", "area")

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("id", "cedula", "nombre", "tel", "cargo", "nivelPro", "salario")
    fields = ( "cedula", "nombre", "tel", "cargo", "nivelPro", "salario")

class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo", "experiencia", "empleado")
    fields = ( "tipo", "experiencia", "empleado")

class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "titulo", "institucion", "fecha", "intensidad_horaria",  "veterinario")
    fields = ( "nombre", "titulo", "institucion", "fecha", "intensidad_horaria", "veterinario")

class GranjaAdmin(admin.ModelAdmin):
    list_display = ("id", "capacidad_max_gallinas", "area", "jefe")
    fields = ( "capacidad_max_gallinas", "area", "jefe")

class GalponAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo", "tipo_zona", "capacidad_max_gallinas", "granja", "responsable")
    fields = ("codigo", "tipo_zona", "capacidad_max_gallinas", "granja", "responsable")

class EventoGalponAdmin (admin.ModelAdmin):
    list_display = ("id", "descripcion", "fecha", "galpon")
    fields = ( "descripcion", "fecha", "galpon")

class LoteAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo", "cantidad_gallinas", "fecha_nacimiento_gallinas", "galpon")
    fields = ( "codigo", "cantidad_gallinas", "fecha_nacimiento_gallinas", "galpon")

class GallinaAdmin(admin.ModelAdmin):
    list_display = ("id", "edad", "raza", "fecha_nacimiento", "novedad", "proceso", "lote")
    fields = ( "edad", "raza", "fecha_nacimiento", "novedad", "proceso", "lote")

class TratamientoAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion", "gallina", "fecha")
    fields = ( "edad", "descripcion", "gallina", "fecha")

class VacunaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "novedad", "fecha", "asistente", "gallina")
    fields = ("nombre", "novedad", "fecha", "asistente", "gallina")


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Cargo,CargoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Granja, GranjaAdmin)
admin.site.register(Galpon, GalponAdmin)
admin.site.register(EventoGalpon, EventoGalponAdmin )
admin.site.register(Lote, LoteAdmin)
admin.site.register(Gallina, GallinaAdmin)
admin.site.register(Vacuna, VacunaAdmin)
admin.site.register(Tratamiento,TratamientoAdmin)

# Register your models here.
