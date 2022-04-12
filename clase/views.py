from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from clase.models import Post
from clase.forms import BusquedaPost, PostFormulario
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


# Create your views here.


    
    
    #return render(request, 'clase/formulario_curso.html', {})

@login_required
def busqueda_post(request):
    post_buscados = []
    dato = request.GET.get('partial_post', None)
    
    if dato is not None:
        post_buscados = Post.objects.filter(titulo__icontains=dato)
    
    buscador = BusquedaPost()
    return render(
        request, "clase/buscador.html",
        {'buscador': buscador, 'post_buscados': post_buscados, 'dato': dato}
    )
    
    
    
    # CRUD basico
    

@login_required    
def listado_post(request):
    listado_post = Post.objects.all()
    return render(
        request, "clase/listado_post.html",
        {'listado_post': listado_post} 
    )
    
    
@login_required  
def crear_post(request):
    if request.method == 'POST':
        formulario = PostFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_post = Post(titulo=data['titulo'], post=data['post'], autor=data['autor'], pic=data['pic'])
            nuevo_post.save()
           #return render(request, 'clase/listado_estudinates.html', {})
            return redirect('listado_post')
            
    formulario = PostFormulario()
    return render(request, 'clase/crear_post.html', {'formulario': formulario})   

@login_required
def actualizar_post(request, id):
    
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = PostFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            post.titulo = data['titulo']
            post.post = data['post']
            post.autor = data['autor']
            post.pic = data['pic']
            post.save()

            return redirect('listado_post')
            
    formulario = PostFormulario(initial={
        'titulo' : post.titulo,
        'post' : post.post, 
        'autor' : post.autor,
        'pic' : post.pic
    })
    return render(request, 'clase/actualizar_post.html', {'formulario': formulario, 'post': post})      

@login_required
def borrar_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('listado_post')

class DetallePost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "clase/detalle_post.html"
    
