from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import  User
from django.http import  HttpResponse
from forms import Loginform,  RegistroClienteform
from .models import Cliente
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
                cc = int(request.POST['cc'])
                user = request.POST['username']
                email = request.POST['email']
                usuario = User.objects.create_user(username = user, email = email, password = p1)
            except :
                context['error'] = 'El usuario ya existe'
                return render(request,'vuelos/signup.html',context)
            try:

                cliente = Cliente(cc=cc,vuelos_disponibles=2, usuario_dj = usuario)
                cliente.save()
                return redirect('/')
            except :
                usuario.delete()
                context['error'] = 'El usuario ya existe'
                return render(request,'vuelos/signup.html',context)

        else:
            context['error'] = 'Las contraseñas no coinciden'
            return render(request,'vuelos/signup.html',context)
    else:
        return render(request,'vuelos/signup.html',{'form':form})

def perfil(request):
    return render(request, 'vuelos/perfil.html')
