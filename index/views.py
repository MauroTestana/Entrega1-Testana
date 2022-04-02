from re import U
from django.http import HttpResponse
from django.shortcuts import render #redirect
#from django.template import loader
#from django.contrib.auth import login as django_login, authenticate
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth.decorators import login_required

#from accounts.forms import NuestraCreacionUser


# Create your views here.

def index(request):
    #return HttpResponse('<h1>Esta es una pag de django</h1>')
    return render(request, 'index/index.html', {})

#def plantilla(request):
    
    #template = loader.get_template('plantilla.html')
    
    datos = {
 #       'lista': ['primero', 'segundo', 'tercero'],
  #      'nombre': 'Juan'
    }
    
    #plantilla_generada = template.render(datos)
    
    #return HttpResponse(plantilla_generada)
    
    return render(request, 'index/plantilla.html', datos)


#def login(request):
    
#    if request.method == 'POST':
#        form = AuthenticationForm(request, data=request.POST)    
        
#        if form.is_valid():
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password']
            
#            user = authenticate(username=username, password=password)
            
#            if user is not None:
#                django_login(request, user)
#                return render(request, 'index/index.html', {'msj': 'Te logueaste correctamente'})
#            else:
#                return render(request, 'index/login.html', {'form': form, 'msj': 'No se autenticó'})
            
            
#        else:
#            return render(request, 'index/login.html', {'form': form, 'msj': 'Datos con formato incorrectos'})
        
#    else:
#        form = AuthenticationForm()
    
#        return render(request, 'index/login.html', {'form': form, 'msj':''})
        #return redirect('login', {})
        
        
#def registrar(request):
    
#    if request.method == 'POST':
#        form = NuestraCreacionUser(request.POST)
        
#        if form.is_valid():
#            username = form.cleaned_data['username']
#            form.save()
#            return render(request, 'index/index.html', {'msj': f'Se creo el usuario {username}'})
#        else:
#             return render(request, 'index/registrar.html', {'form':form, 'msj': ''})    
    
#    form = NuestraCreacionUser()
#    return render(request,  'index/registrar.html', {'form': form, 'msj':''})