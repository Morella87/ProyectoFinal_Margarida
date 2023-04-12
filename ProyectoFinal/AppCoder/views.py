from AppCoder.forms import (AvatarFormulario, CreadorFormulario,
                            PropietarioFormulario, TextoFormulario,
                            UserEditForm, UserRegisterForm)
from AppCoder.models import Avatar, Creador, Propietario, Texto, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import *

# Create your views here.
#------Login------#

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, 'inicio.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'inicio.html', {"mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request, 'inicio.html', {"mensaje": "No se pudo iniciar sesión, datos incorrectos"})
        
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

#------registro------#

def register(request):
    if request.method == 'POST':            
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'inicio.html',  {"mensaje":"Usuario Creado :)"})
    else:       
       form = UserRegisterForm()     
    return render(request,'registro.html',  {"form":form})

#------Perfil de usuario------#

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(miFormulario)
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {"mensaje":"Contraseña incorrecta."})
            
            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, 'editarPerfil.html', {'miFormulario':miFormulario, 'usuario':usuario})

#------Inicio y Avatar------#

def inicio(request):
    return render(request,'inicio.html')

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,'inicio.html', {'url':avatares[0].imagen.url})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'agregarAvatar.html', {'miFormulario':miFormulario})

#------Vistas y edicion de Libros------#
def texto(request):
    return render(request,'texto.html')

@login_required
def leerLibro(request):
    libros = Texto.objects.all()
    contexto = {'libros':libros}
    return render(request,'texto.html',contexto)

def formularioLibro(request):
    if request.method == 'POST':
        miFormularioLibro = TextoFormulario(request.POST, request.FILES)
        print(miFormularioLibro)

        if miFormularioLibro.is_valid:
            
            informacion = miFormularioLibro.cleaned_data		    
            libro = Texto(tituloLibro=informacion['tituloLibro'], 
            autor=informacion['autor'],
            edicion=informacion['edicion'], 
            genero=informacion['genero'], 
            editorial=informacion['editorial'],
            disponible=informacion['disponible'], 
            tapaLibro=request.FILES['tapaLibro'])
        		    
            libro.save()

            libros = Texto.objects.all()    
            return render(request,'texto.html',{'libros':libros})

    else:
        miFormularioLibro = TextoFormulario()
    return render(request, 'formularioLibro.html',{"miFormularioLibro":miFormularioLibro})

def editarLibro(request,libro_titulo):

    libro = Texto.objects.get(tituloLibro = libro_titulo)

    if request.method == 'POST':
        miFormularioLibro = TextoFormulario(request.POST, request.FILES)
        print(miFormularioLibro)

        if miFormularioLibro.is_valid():
            
            informacion = miFormularioLibro.cleaned_data
		    
            libro.tituloLibro=informacion['tituloLibro']
            libro.autor=informacion['autor']
            libro.edicion=informacion['edicion']
            libro.genero=informacion['genero']
            libro.editorial=informacion['editorial']
            libro.disponible=informacion['disponible']
            libro.tapaLibro=request.FILES['tapaLibro']
            		    
            libro.save()
            libros = Texto.objects.all()
            return render(request, 'texto.html',{'libros':libros})

    else:
        miFormularioLibro= TextoFormulario(initial={'tituloLibro': libro.tituloLibro, 'autor': libro.autor,
            'edicion': libro.edicion, 'genero': libro.genero,'editorial': libro.editorial,
            'disponible': libro.disponible, 'tapaLibro':libro.tapaLibro}) 
    
    return render(request, 'editarLibro.html', {'miFormularioLibro': miFormularioLibro, 'libro_titulo':libro_titulo})
        
def eliminarLibro(request,libro_titulo):
    libro = Texto.objects.get(tituloLibro = libro_titulo)
    libro.delete()
    libros = Texto.objects.all()
    contexto ={'libros':libros}
    return render(request,'texto.html',contexto)

#------buscar libros------#

@login_required
def busquedaLibro(request):
    return render(request,'busquedaLibro.html')

@login_required
def buscar(request):
    
    if request.GET['tituloLibro']:
        tituloLibro = request.GET['tituloLibro']
        libros = Texto.objects.filter(tituloLibro__icontains=tituloLibro)

        return render(request, 'texto.html', {'libros':libros})

    else:
        respuesta = 'No enviaste datos'
    return render(request, 'inicio.html', {'respuesta':respuesta})

#------Vistas y edicion de Propietarios ------#

def propietario(request):
    return render(request,'propietario.html')

@login_required
def leerPropietario(request):
    propietarios = Propietario.objects.all()
    contexto = {"propietarios":propietarios}
    return render(request,'propietario.html',contexto)

def formularioPropietario(request):

    if request.method == 'POST':
        miFormularioPropietario = PropietarioFormulario(request.POST)
        print(miFormularioPropietario)

        if miFormularioPropietario.is_valid:
            
            informacion = miFormularioPropietario.cleaned_data
		    
            propietario = Propietario(nombre=informacion['nombre'],apellido=informacion['apellido'],
                telefono=informacion['telefono'],email=informacion['email'],tituloLibro=informacion['tituloLibro'])
		    
            propietario.save()

            propietarios = Propietario.objects.all()
            
            return render(request,'propietario.html',{"propietarios":propietarios})

    else:
        miFormularioPropietario = PropietarioFormulario()
    return render(request, 'formularioPropietario.html',{"miFormularioPropietario":miFormularioPropietario})

def editarPropietario(request,propietario_nombre):

    propietario = Propietario.objects.get(nombre = propietario_nombre)

    if request.method == 'POST':
        miFormularioPropietario = PropietarioFormulario(request.POST)
        print(miFormularioPropietario)

        if miFormularioPropietario.is_valid:
            
            informacion = miFormularioPropietario.cleaned_data
		    
            propietario.nombre=informacion['nombre']
            propietario.apellido=informacion['apellido']
            propietario.telefono=informacion['telefono']
            propietario.email=informacion['email']
            propietario.tituloLibro=informacion['tituloLibro']
		    
            propietario.save()
            
            return render(request, 'inicio.html')

    else:
        miFormularioPropietario= PropietarioFormulario(initial={'nombre': propietario.nombre, 'apellido':propietario.apellido , 
            'telefono':propietario.telefono, 'email':propietario.email, 'tituloLibro':propietario.tituloLibro}) 
    
    return render(request, 'editarPropietario.html', {"miFormularioPropietario": miFormularioPropietario, "propietario_nombre":propietario_nombre})
        
def eliminarPropietario(request,propietario_nombre):
    propietario = Propietario.objects.get(nombre=propietario_nombre)
    propietario.delete()
    propietarios = Propietario.objects.all()
    contexto ={"propietarios":propietarios}
    return render(request,'propietario.html',contexto)

#------Vistas y edicion de Autor------#

def autor(request):
    return render(request,'autor.html')

@login_required
def leerAutor(request):
    autores = Creador.objects.all()
    contexto = {"autores":autores}
    return render(request,'autor.html',contexto)

def formularioAutor(request):

    if request.method == 'POST':
        miFormularioAutor = CreadorFormulario(request.POST)
        print(miFormularioAutor)

        if miFormularioAutor.is_valid:
            
            informacion = miFormularioAutor.cleaned_data
		    
            autor = Creador(nombreaut=informacion['nombreaut'],
            apellidoaut=informacion['apellidoaut'],tituloLibro=informacion['tituloLibro'])
		    
            autor.save()

            autores = Creador.objects.all()
            
            contexto = {"autores":autores}
            return render(request,'autor.html',contexto)

    else:
        miFormularioAutor = CreadorFormulario()
    return render(request, 'formularioAutor.html',{"miFormularioAutor":miFormularioAutor})

def editarAutor(request,autor_nombre):

    autor = Creador.objects.get(nombreaut = autor_nombre)

    if request.method == 'POST':
        miFormularioAutor = CreadorFormulario(request.POST)
        print(miFormularioAutor)

        if miFormularioAutor.is_valid:
            
            informacion = miFormularioAutor.cleaned_data
		    
            autor.nombreaut=informacion['nombreaut']
            autor.apellidoaut=informacion['apellido']
            autor.tituloLibro=informacion['tituloLibro']
		    
            autor.save()
            
            return render(request, 'inicio.html')

    else:
        miFormularioAutor= CreadorFormulario(initial={'Nombre Autor': autor.nombreaut, 'Apellido Autor':autor.apellidoaut , 'Titulo del libro':autor.tituloLibro}) 
    
    return render(request, 'editarAutor.html', {"miFormularioAutor": miFormularioAutor, "autor_nombre":autor_nombre})
        
        
def eliminarAutor(request,autor_nombre):
    autor = Creador.objects.get(nombreaut = autor_nombre)
    autor.delete()
    autores = Creador.objects.all()
    contexto ={"autores":autores}
    return render(request,'autor.html',contexto)

