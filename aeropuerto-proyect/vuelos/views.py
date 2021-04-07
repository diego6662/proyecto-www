from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import  User
from forms import Loginform, Aerolineaform, RegistroClienteform 
from .models import Aerolinea
from django.http import  HttpResponse
from django.contrib import messages
from forms import Loginform, Aerolineaform, Vueloform, Escalaform 
from .models import Aerolinea, Vuelo, Escala
# Create your views here.

def index(request):
    vuelos = Vuelo.objects.all()
    context = {
            'vuelos':vuelos,
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
        return redirect('/')

    else:
        return render(request,'vuelos/registrarAero.html',context)


def registrar_vuelo(request):
    form = Vueloform()
    aerolineas = Aerolinea.objects.all()
    context = {
            'form':form,
            'aero':aerolineas
            }
    if request.method == 'POST':
        id_vuelo = request.POST['id_vuelo']                
        id_aero = int(request.POST['id_aerolinea'])
        destino = request.POST['destino']
        costo = float(request.POST['costo'])
        aerolinea = Aerolinea.objects.get(pk = id_aero)
        vuelo = Vuelo(id_vuelo=id_vuelo,aerolinea=aerolinea,destino=destino,costo=costo)
        vuelo.save()
        return redirect('vuelos:registrar-escala',id_vuelo)
    else:
        return render(request,'vuelos/registroVuelo.html',context)

def registrar_escala(request,id):
    form = Escalaform()
    context = {
            'id':id,
            'form':form
            }
    if request.method == 'POST':
        vuelo = Vuelo.objects.get(pk = id)
        fecha_salida = f"{request.POST['fecha_salida_year']}-{request.POST['fecha_salida_month']}-{request.POST['fecha_salida_day']}"
        fecha_llegada = f"{request.POST['fecha_llegada_year']}-{request.POST['fecha_llegada_month']}-{request.POST['fecha_llegada_day']}"
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
            'form':form
            }
    if request.method == 'POST':
        aerolinea = Aerolinea.objects.get(pk=id)
        nombre = request.POST['aerolinea']
        aerolinea.nombre = nombre
        aerolinea.save()
        return redirect('/')
    else:
        return render(request,'vuelos/modificarAero.html',context)

def vista_vuelo(request,id):
    vuelo = Vuelo.objects.get(pk=id)
    escalas = Escala.objects.filter(vuelo = id)
    context = {
            'vuelo':vuelo,
            'escalas':escalas
            }
    return render(request,'vuelos/vuelo.html',context)
