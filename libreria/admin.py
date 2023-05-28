from django.contrib import admin
from .models import Estudiante, Prestamo, Materia, Autor, Editorial, Libro, Configuracion, DetallePermiso

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'ine', 'nombre', 'carrera', 'direccion', 'telefono', 'estado')
    list_editable = ('estado',)


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'libro', 'fecha_prestamo', 'fecha_devolucion', 'cantidad', 'observacion', 'estado')
    list_editable = ('estado',)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'materia', 'estado')
    list_editable = ('estado',)



class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'imagen', 'estado')
    list_editable = ('estado',)


class EditorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'editorial', 'estado')
    list_editable = ('estado',)


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cantidad', 'autor', 'editorial', 'materia', 'foto', 'estado')
    list_editable = ('estado',)


class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion', 'correo', 'foto')
    

class DetallePermisoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'permiso')
    list_editable = ('estado',)


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(DetallePermiso, DetallePermisoAdmin)