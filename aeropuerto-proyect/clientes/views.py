from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.http import  HttpResponse
from django.contrib.auth.decorators import  login_required
from forms import Loginform,  RegistroClienteform, editar_perfilForm
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

    if request.method == 'POST':
        # si trae post se carga el formulario con 
        form = RegistroClienteform(request.POST)

        # validoacion del formulario
        if form.is_valid():
            # cera un objeto del modelo
            usr = User()
            # se carga con la data
            usr.first_name = request.POST['nombre']
            usr.last_name  = request.POST['apellido']
            usr.username   = request.POST['username']
            usr.email      = request.POST['email']
            usr.set_password(request.POST['password1'])
            # se guarda en la base de datos
            usr.save()

            # se crea un objeto cliente
            clt = Cliente()
            clt.cc = int(request.POST['cc'])
            clt.vuelos_disponibles = 2
            clt.usuario_dj = usr

            # guardar cliente
            clt.save()

            #redirecion al login
            return redirect('clientes:login')
        else:
            # lo retorna con las correciones pertinentes
            return render(request,'vuelos/signup.html',{'form':form})
    else:
        form = RegistroClienteform()
        return render(request,'vuelos/signup.html',{'form':form})

@login_required
def perfil(request):
    usuario = Cliente.objects.get(usuario_dj = request.user)
    reservas = Reserva.objects.filter(cliente = usuario)
    context = {
            'usuario':usuario,
            'reservas':reservas
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


def usuarios_admin(request):
    all_clientes = Cliente.objects.all()
    context = {"clientes":all_clientes}
    return render(request, 'vuelos/usuariosAdmin.html',context)


# modificar a un cliente desde el admin
def cliente_perfil_admin(request, cliente_id):
    # cliente cargado para la modificacion
    clt = Cliente.objects.get(cc = cliente_id)

    if request.method == 'POST':
        #  hay una petiocion por envio para actualizar
        
        form = RegistroClienteform(request.POST)
        if form.is_valid():
            # si es valido actualizamos
            # tomo el usuario
            usr = clt.usuario_dj
            usr.first_name = request.POST['nombre']
            usr.last_name = request.POST['apellido']
            usr.username = request.POST['username']
            usr.email = request.POST['email']
            #usr.password = request.POST['password2']
            usr.set_password(request.POST['password2'])
            # actualizo
            usr.save()
            #
            return redirect('clientes:usuarios_admin')
        elif form.errors['username']:
            # puedo ignorar el error de mismo usuario, por ser actualizacion
            # tomo el usuario
            usr = clt.usuario_dj
            usr.first_name = request.POST['nombre']
            usr.last_name = request.POST['apellido']
            usr.username = request.POST['username']
            usr.email = request.POST['email']
            #usr.password = request.POST['password2']
            usr.set_password(request.POST['password2'])
            # actualizo
            usr.save()
            #
            return redirect('clientes:usuarios_admin')
        else:
            # hubo errores
            context = { "cliente":clt, "form":form}
            return render(request, 'vuelos/modificar_cliente_admin.html',context)
            
    else:
        # se debe armar el formulario
        # asi que se carga la información del cliente
        form = RegistroClienteform(
            initial={
                'cc': clt.cc,
                'username': clt.usuario_dj.username,
                'nombre' :  clt.usuario_dj.first_name,
                'apellido' :  clt.usuario_dj.last_name,
                'email' : clt.usuario_dj.email,

            })

    context = { "cliente":clt, "form":form}
    return render(request, 'vuelos/modificar_cliente_admin.html',context)

def eliminar_cliente(request, cliente_id):
    cl = Cliente.objects.get(cc=cliente_id)
    if cl:
        usrCl = cl.usuario_dj
        usrCl.delete()

    return redirect('clientes:usuarios_admin')
   
def cancelar_reserva(request,id):
    reserva = Reserva.objects.get(pk=id)
    reserva.delete()
    usuario = Cliente.objects.get(usuario_dj=request.user)
    usuario.vuelos_disponibles += 1
    usuario.save()
    return redirect('clientes:perfil')

def editar_perfil(request):
    form = editar_perfilForm()
    context = {
            'form':form
            }
    if request.method == 'POST':
        usuario = Cliente.objects.get(usuario_dj = request.user)
        usuario.image_perfil = request.FILES['foto']
        usuario.usuario_dj.email = request.POST['email']
        usuario.usuario_dj.first_name = request.POST['nombre']
        usuario.usuario_dj.last_name = request.POST['apellido']
        usuario.usuario_dj.save()
        usuario.save()
        return redirect('clientes:perfil')


    return render(request,'vuelos/modificarPerfil.html',context)
