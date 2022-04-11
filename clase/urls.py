from django.urls import path
from . import views
#from .views import listado_estudiantes, nuevo_curso, formulario_curso, busqueda_curso


urlpatterns = [
    path('nuevo/', views.nuevo_curso, name='nuevo_curso'),
    path('curso/', views.formulario_curso, name= 'formulario_curso'),
    path('buscador/', views.busqueda_curso, name= 'busqueda_curso'),
    
    #path('estudiante/', views.estudiante, name="estudiante"),
    path('post/crear/', views.crear_post, name="crear_post"),
    path('post/borrar/<int:id>', views.borrar_post, name="borrar_post"),
    path('post/<int:pk>', views.DetallePost.as_view(), name="detalle_post"),
    path('post/actualizar/<int:id>', views.actualizar_post, name="actualizar_post"),
    path('post/listado', views.listado_post, name="listado_post")
]
