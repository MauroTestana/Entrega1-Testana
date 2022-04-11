from re import U
from django.http import HttpResponse
from django.shortcuts import render 

#from accounts.forms import NuestraCreacionUser


# Create your views here.

def index(request):
    #return HttpResponse('<h1>Esta es una pag de django</h1>')
    return render(request, 'index/index.html', {})

def about(request):
    return render(request, 'index/about.html', {})