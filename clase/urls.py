from django.urls import path
from . import views
#from .views import listado_estudiantes, nuevo_curso, formulario_curso, busqueda_curso


urlpatterns = [
    path('buscador/', views.busqueda_post, name= 'busqueda_post'),
    
    #path('estudiante/', views.estudiante, name="estudiante"),
    path('post/crear/', views.crear_post, name="crear_post"),
    path('post/borrar/<int:id>', views.borrar_post, name="borrar_post"),
    path('post/<int:pk>', views.DetallePost.as_view(), name="detalle_post"),
    path('post/actualizar/<int:id>', views.actualizar_post, name="actualizar_post"),
    path('post/listado', views.listado_post, name="listado_post")
]
