from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import  User
from forms import Loginform, Aerolineaform, Vueloform
from .models import Aerolinea, Vuelo
# Create your views here.
def index(request):
    return render(request,'vuelos/index.html')

def vuelo(request):
    return render(request,'vuelos/vuelo.html')

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
    a = {'id':id}
    
    return render(request,'vuelos/registroEscala.html',a)
