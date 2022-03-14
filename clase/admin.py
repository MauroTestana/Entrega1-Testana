from django.contrib import admin

from clase.models import Curso, Entegrables, Estudiantes, Profesor

# Register your models here.

admin.site.register(Estudiantes)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entegrables)
