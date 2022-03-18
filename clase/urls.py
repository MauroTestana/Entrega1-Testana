from django.urls import path
from . import views
#from .views import listado_estudiantes, nuevo_curso, formulario_curso, busqueda_curso


urlpatterns = [
    path('nuevo/', views.nuevo_curso, name='nuevo_curso'),
    path('curso/', views.formulario_curso, name= 'formulario_curso'),
    path('buscador/', views.busqueda_curso, name= 'busqueda_curso'),
    
    #path('estudiante/', views.estudiante, name="estudiante"),
    path('estudiante/crear', views.crear_estudiante, name="crear_estudiante"),
    #path('estudiante/borrar', views.borrar_estudiante, name="borrar_estudiante"),
    path('estudiante/actualizar/<id>', views.actualizar_estudiante, name="actualizar_estudiante"),
    path('estudiante/listado', views.listado_estudiantes, name="listado_estudiantes")
]
