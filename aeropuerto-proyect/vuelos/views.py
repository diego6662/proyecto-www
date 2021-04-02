from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import  User
from forms import Loginform, Aerolineaform, RegistroClienteform 
from .models import Aerolinea
from django.http import  HttpResponse
from forms import Loginform, Aerolineaform, Vueloform, Escalaform 
from .models import Aerolinea, Vuelo
# Create your views here.

def index(request):
    return render(request,'vuelos/index.html')

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
        costo = float(request.POST['costo'])
        aerolinea = Aerolinea.objects.get(pk = id_aero)
        vuelo = Vuelo(id_vuelo=id_vuelo,aerolinea=aerolinea,costo=costo)
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
        pass
    else:
        return render(request,'vuelos/registroEscala.html',context)
