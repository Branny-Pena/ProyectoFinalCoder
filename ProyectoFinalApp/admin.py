from django.contrib import admin
from .models import *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'comision')
    search_fields = ('nombre', 'comision')


class EstudianteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido')


class ProfesorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'profesion')
    readonly_fields = ('profesion',)


admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)