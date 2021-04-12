from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import  User
from forms import Loginform, Aerolineaform, RegistroClienteform 
from .models import Aerolinea
from django.http import  HttpResponse
from django.contrib import messages
from forms import Loginform, Aerolineaform, Vueloform, Escalaform, CiudadForm
from .models import Aerolinea, Vuelo, Escala, Ciudades

from clientes.models import Cliente
import requests
# Create your views here.

def index(request):
    vuelos = Vuelo.objects.all()
    user = request.user
    admin = user.is_staff
    if str(user) == 'AnonymousUser' :
        user = None
    context = {
            'vuelos':vuelos,
            'user':user,
            'admin':admin,
            }
    return render(request,'vuelos/index.html',context)

def vuelo(request):
    return render(request,'vuelos/vuelo.html')



def registrar_aerolinea(request):
    form = Aerolineaform()
    context = {
            'form':form 
            }
    if request.method == 'POST':
        nombre = request.POST['aerolinea']
        aerolinea = Aerolinea(nombre=nombre)
        aerolinea.save()
        return redirect('vuelos:aerolineas')

    else:
        return render(request,'vuelos/registrarAero.html',context)


def registrar_vuelo(request):
    form = Vueloform()
    aerolineas = Aerolinea.objects.all()
    dias = [i for i in range(1,31)]
    context = {
            'form':form,
            'aero':aerolineas,
            'dias':dias
            }
    if request.method == 'POST':
        id_vuelo = request.POST['id_vuelo']                
        id_aero = int(request.POST['id_aerolinea'])
        destino = int(request.POST['destino'])
        costo = float(request.POST['costo'])
        aerolinea = Aerolinea.objects.get(pk = id_aero)
        destino = Ciudades.objects.get(pk = destino)
        requisitos = request.POST['requisitos']
        fecha = request.POST['fecha_vuelo']
        hora = request.POST['hora_vuelo']
        fecha = f'2021-04-{fecha} {hora}'
        vuelo = Vuelo(id_vuelo=id_vuelo,aerolinea=aerolinea,destino=destino,costo=costo,fecha=fecha,requisitos=requisitos)
        vuelo.save()
        return redirect('vuelos:registrar-escala',id_vuelo)
    else:
        return render(request,'vuelos/registroVuelo.html',context)

def registrar_escala(request,id):
    form = Escalaform()
    dias = [i for i in range(1,31)]
    context = {
            'id':id,
            'form':form,
            'dias':dias
            }
    if request.method == 'POST':
        vuelo = Vuelo.objects.get(pk = id)
        fecha_salida = f"2021-04-{request.POST['fecha_salida']}"
        fecha_llegada = f"2021-04-{request.POST['fecha_llegada']}"
        escala = Escala(vuelo=vuelo,
                nombre_procedencia=request.POST['procedencia'],
                cod_procedencia=request.POST['postal_procedencia'],
                nombre_destino=request.POST['destino'],
                cod_destino=request.POST['postal_destino'],
                fecha_salida=fecha_salida,
                fecha_llegada=fecha_llegada,
                requisitos=request.POST['requisitos'])
        escala.save()
        return redirect('vuelos:registrar-escala',id)
    else:
        return render(request,'vuelos/registroEscala.html',context)

def modificar_aerolinea(request,id):
    form = Aerolineaform()
    context = {
            'form':form,
            'id':id
            }
    if request.method == 'POST':
        aerolinea = Aerolinea.objects.get(pk=id)
        nombre = request.POST['aerolinea']
        aerolinea.nombre = nombre
        aerolinea.save()
        return redirect('/')
    else:
        return render(request,'vuelos/modificarAero.html',context)


@login_required
def vista_vuelo(request,id):

    vuelo = Vuelo.objects.get(pk=id)
    escalas = Escala.objects.filter(vuelo = id)
    context = {
            'vuelo':vuelo,
            'escalas':escalas
            }
    if User.is_authenticated:
        usr = request.user
        clt = Cliente.objects.get(usuario_dj= usr)
        reservas_diponibles = clt.vuelos_disponibles
        context['reservas_diponibles'] = reservas_diponibles

    return render(request,'vuelos/vuelo.html',context)


def vuelo_admin(request,id):
    vuelo = Vuelo.objects.get(pk=id)
    escalas = Escala.objects.filter(vuelo = id)
    context = {
            'vuelo':vuelo,
            'escalas':escalas
            }
    return render(request,'vuelos/vuelo_admin.html',context)

def eliminar_vuelo(request,id):
    if request.method == 'POST':
        vuelo = Vuelo.objects.get(pk=id)
        vuelo.delete()
        return redirect('/')
    else:
        return render(request, 'vuelos/eliminarVuelo.html')

def editar_vuelo(request,id):
    form = Vueloform()
    aerolineas = Aerolinea.objects.all()
    dias = [i for i in range(1,31)]
    context = {
            'form':form,
            'aero':aerolineas,
            'dias':dias
            }
    if request.method == 'POST':
        id_aero = int(request.POST['id_aerolinea'])
        destino = request.POST['destino']
        costo = float(request.POST['costo'])
        aerolinea = Aerolinea.objects.get(pk = id_aero)
        fecha = request.POST['fecha_vuelo']
        destino = int(request.POST['destino'])
        destino = Ciudades.objects.get(pk=destino)
        requisitos = request.POST['requisitos']
        hora = request.POST['hora_vuelo']
        fecha = f'2020-04-{fecha} {hora}'
        vuelo = Vuelo(id_vuelo=id,aerolinea=aerolinea,destino=destino,costo=costo,fecha=fecha,requisitos=requisitos)
        vuelo.save()
        escalas = Escala.objects.filter(vuelo=id)
        escalas.delete()
        return redirect('vuelos:registrar-escala',id)
    else:
        return render(request,'vuelos/editarVuelo.html',context)



def aerolineas(request):
    aerolineas = Aerolinea.objects.all()
    context = {
            'aerolineas':aerolineas
            }
    return render(request,'vuelos/aerolineas.html',context)

def eliminar_aerolinea(request,id):
    aerolinea = Aerolinea.objects.get(pk=id)
    aerolinea.delete()
    return redirect('/')

def registrar_ciudad(request):
    form = CiudadForm()
    context = {
            'form':form,
            }
    if request.method == 'POST':
        form = CiudadForm(request.POST,request.FILES)
        postal = request.POST['postal']
        nombre = request.POST['nombre']
        foto = request.FILES['foto']
        ciudad = Ciudades(postal=postal, nombre=nombre,foto=foto)
        ciudad.save()
        return redirect('vuelos:ciudades')
    else:
        return render(request,'vuelos/registrarCiudad.html',context)

def modificar_ciudad(request,id):
    form = CiudadForm()
    ciud = Ciudades.objects.get(postal=id)
    context = {
            'form':form,
            'id':id
            }
    
    if request.method == 'POST':
        ciudad = Ciudades.objects.get(pk=id)
        nombre = request.POST['ciudad']
        postal = request.POST['postal']
        ciudad.nombre = nombre
        ciudad.postal = postal
        ciudad.save()
        return redirect('vuelos:ciudades')
    else:
        form = CiudadForm(
            initial={
                'postal': ciud.postal,
                'nombre': ciud.nombre,
                'foto' :  ciud.foto,
            })
        return render(request,'vuelos/modificarCiudad.html',{"form":form, 'id':id})

def ciudades(request):
    ciudades = Ciudades.objects.all()
    context = {
            'ciudades':ciudades
            }
    return render(request,'vuelos/ciudad.html',context)

def clima(request,postal):
    #https://api.openweathermap.org/data/2.5/weather?zip=763041,co&appid=dfa2f824fc036ff5f2f9c022f70c4a7c&lang=es&units=metric
    req = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+str(postal)+',co&appid=dfa2f824fc036ff5f2f9c022f70c4a7c&lang=es&units=metric')
    json_object = req.json()

    descripcion = json_object['weather'][0]['description']
    tempertura = json_object['main']['temp']
    tempertura_min = json_object['main']['temp_min']
    tempertura_max = json_object['main']['temp_max']
    presion = json_object['main']['pressure']
    humedad = json_object['main']['humidity']
    viento_velocidad =  json_object['wind']['speed']
    viento_deg =  json_object['wind']['deg']
    ciudad = json_object['name']

    context = {
        "descripcion":descripcion,
        "tempertura":tempertura,
        "tempertura_max":tempertura_max,
        "tempertura_min":tempertura_min,
        "presion":presion,
        "humedad":humedad,
        "viento_velocidad":viento_velocidad,
        "viento_deg":viento_deg,
        "ciudad":ciudad
    }
    return render(request,'vuelos/clima.html',context)  