from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    #return HttpResponse('<h1>Esta es una pag de django</h1>')
    return render(request, 'index/index.html', {})

def plantilla(request):
    
    #template = loader.get_template('plantilla.html')
    
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Juan'
    }
    
    #plantilla_generada = template.render(datos)
    
    #return HttpResponse(plantilla_generada)
    
    return render(request, 'index/plantilla.html', datos)


def login(request):
    
    #return render(request, 'index/index.html', {})
    return redirect('login', {})