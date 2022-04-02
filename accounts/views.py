from django.shortcuts import render, redirect
from accounts.forms import NuestraCreacionUser
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import NuestraCreacionUser

# Create your views here.


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)    
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return render(request, 'index/index.html', {'msj': 'Te logueaste correctamente'})
            else:
                return render(request, 'accounts/login.html', {'form': form, 'msj': 'No se autenticó'})
            
            
        else:
            return render(request, 'accounts/login.html', {'form': form, 'msj': 'Datos con formato incorrectos'})
        
    else:
        form = AuthenticationForm()
    
        return render(request, 'accounts/login.html', {'form': form, 'msj':''})
        #return redirect('login', {})
        
        
def registrar(request):
    
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index/index.html', {'msj': f'Se creo el usuario {username}'})
        else:
             return render(request, 'accounts/registrar.html', {'form':form, 'msj': ''})    
    
    form = NuestraCreacionUser()
    return render(request,  'accounts/registrar.html', {'form': form, 'msj':''})
