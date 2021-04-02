from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from vuelos.models import Aerolinea
class Loginform(forms.Form):
    usuario = forms.CharField(max_length=20,label='Nombre de usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput(),
            label='Contraseña')


class RegistroClienteform(forms.Form):
    cc = forms.IntegerField(required=True,label='Identificacion')
    username = forms.CharField(max_length=20,required=True )
    email = forms.EmailField(max_length=30,required=True ,label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(),label="Confirmar Contraseña")

class Aerolineaform(forms.Form):
    aerolinea = forms.CharField(max_length=20, label='Nombre aerolinea')


class Vueloform(forms.Form):
    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo')
    id_aerolinea = forms.ModelChoiceField(Aerolinea.objects.all())
    costo = forms.FloatField(label='Precio')


class Escalaform(forms.Form):
#    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo',)
    postal_procedencia = forms.IntegerField(label='Codigo postal procedencia')
    postal_destino = forms.IntegerField(label='Codigo postal destino')
    fecha_salida = forms.DateField(label='Fecha de salida', widget = forms.SelectDateWidget(years=[2021],months={3:'Abril'},))
    fecha_llegada = forms.DateField(label='Fecha de llegada', widget = forms.SelectDateWidget(years=[2021],months={3:'Abril'}))
    requisitos = forms.CharField(widget=forms.Textarea, label='Requisitos')


