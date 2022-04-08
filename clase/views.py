from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from clase.models import Curso, Estudiantes
from clase.forms import CursoFormulario, BusquedaCurso, EstudianteFormulario
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


# Create your views here.

@login_required
def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Python', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo  el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")

@login_required
def formulario_curso(request):
    
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            return render(request, 'index/index.html', {'nuevo_curso': nuevo_curso})
            
    formulario = CursoFormulario()
    return render(request, 'clase/formulario_curso.html', {'formulario': formulario})
    
    
    #return render(request, 'clase/formulario_curso.html', {})

@login_required
def busqueda_curso(request):
    cursos_buscados = []
    dato = request.GET.get('partial_curso', None)
    
    if dato is not None:
        cursos_buscados = Curso.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaCurso()
    return render(
        request, "clase/buscador.html",
        {'buscador': buscador, 'cursos_buscados': cursos_buscados, 'dato': dato}
    )
    
    
    
    # CRUD basico
    

@login_required    
def listado_estudiantes(request):
    listado_estudiantes = Estudiantes.objects.all()
    return render(
        request, "clase/listado_estudiantes.html",
        {'listado_estudiantes': listado_estudiantes} 
    )
    
    
@login_required  
def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_estudiante = Estudiantes(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], pic=data['pic'])
            nuevo_estudiante.save()
           #return render(request, 'clase/listado_estudinates.html', {})
            return redirect('listado_estudiantes')
            
    formulario = EstudianteFormulario()
    return render(request, 'clase/crear_estudiante.html', {'formulario': formulario})   

@login_required
def actualizar_estudiante(request, id):
    
    estudiante = Estudiantes.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
           #return render(request, 'clase/listado_estudinates.html', {})
            return redirect('listado_estudiantes')
            
    formulario = EstudianteFormulario(initial={
        'nombre' : estudiante.nombre,
        'apellido' : estudiante.apellido, 
        'email' : estudiante.email
    })
    return render(request, 'clase/actualizar_estudiante.html', {'formulario': formulario, 'estudiante': estudiante})      

@login_required
def borrar_estudiante(request, id):
    estudiante = Estudiantes.objects.get(id=id)
    estudiante.delete()
    return redirect('listado_estudiantes')

class DetalleEstudiante(LoginRequiredMixin, DetailView):
    model = Estudiantes
    template_name = "clase/detalle_estudiante.html"