from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from clase.models import Curso, Estudiantes
from clase.forms import CursoFormulario, BusquedaCurso, EstudianteFormulario
import random

# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Python', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo  el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")

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
    
def listado_estudiantes(request):
    listado_estudiantes = Estudiantes.objects.all()
    return render(
        request, "clase/listado_estudiantes.html",
        {'listado_estudiantes': listado_estudiantes} 
    )
    
    
    
def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_estudiante = Estudiantes(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            nuevo_estudiante.save()
           #return render(request, 'clase/listado_estudinates.html', {})
            return redirect('listado_estudiantes')
            
    formulario = EstudianteFormulario()
    return render(request, 'clase/crear_estudiante.html', {'formulario': formulario})   

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
            
    formulario = EstudianteFormulario()
    return render(request, 'clase/actualizar_estudiante.html', {'formulario': formulario})      