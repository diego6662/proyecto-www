from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.http import  HttpResponse
from django.contrib.auth.decorators import  login_required
from forms import Loginform,  RegistroClienteform
from django.contrib.auth.models import  User
from .models import Cliente,Reserva
from vuelos.models import Vuelo
from django.contrib import messages
#
# Create your views here.
def login(request):
    form = Loginform()
    context = {
            'form':form
            }
    if request.method == 'GET':
        return render(request,'vuelos/login.html',context)
    else:
        user = request.POST['usuario']
        contrasena = request.POST['contrasena']
        auth = authenticate(request,username=user,password=contrasena)
        if auth:
            auth_login(request,auth)
            return redirect('/')
        else:
            context['error'] = 'Usuario no registrado'
            return render(request,'vuelos/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/')

def registrar_usuario(request):
    form = RegistroClienteform()
    context = {
            'form':form
            }
    if request.method == 'POST':
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            try:
                cce = int(request.POST['cc'])
                user = request.POST['username']
                email = request.POST['email']
                nombre = request.POST['nombre']
                apellido = request.POST['apellido']
                usuario = User.objects.create_user(username = user, email = email, first_name = nombre, last_name=apellido,password = p1)
                usuario.save()
            except :
                context['error'] = 'El usuario ya existe'
                return render(request,'vuelos/signup.html',context)
            try:
                usuario = User.objects.get(username=user)
                obj,create = Cliente.objects.get_or_create(cc=cce,vuelos_disponibles=2, usuario_dj = usuario)
                #obj.save()
                messages.success(request,'Usuario creado con exito')
                return redirect('clientes:login')
            except :
                usuario.delete()
                context['error'] = 'El usuario ya existe'
                return render(request,'vuelos/signup.html',context)

        else:
            context['error'] = 'Las contraseñas no coinciden'
            return render(request,'vuelos/signup.html',context)
    else:
        return render(request,'vuelos/signup.html',{'form':form})

@login_required
def perfil(request):
    usuario = Cliente.objects.get(usuario_dj = request.user)
    context = {
            'usuario':usuario
            }
    return render(request, 'vuelos/perfil.html',context)

def reserva(request,vuelo):
    usuario = Cliente.objects.get(usuario_dj = request.user)
    vuelo =  Vuelo.objects.get(pk = vuelo)
    if usuario.vuelos_disponibles > 0:
        reserva = Reserva.objects.create(cliente = usuario,vuelo = vuelo)
        usuario.vuelos_disponibles -= 1
        usuario.save()
        messages.success(request,'Reserva realizada con exito')
    else:
        messages.success(request,'Ya utilizo todas sus reservas disponibles')

    return redirect('/')

