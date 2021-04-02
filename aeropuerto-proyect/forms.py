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

    def clean(self):
        cd = self.get.cleaned_data

        psswrd1 = cd.get("password1")
        psswrd2 = cd.get("password2")
        #username = cd.get("username")
        cc = cd.get("cc")
        number_same_users = User.objects.filter(username=cd.get('username')).count()

        if  psswrd1 != psswrd2:
            raise ValidationError("Las claves no coinciden")
        elif int(cc) < 0 or len(cc) < 8:
            raise ValidationError("La identificacion debe tener almenos 8 digitos")
        elif number_same_users > 0: 
            raise ValidationError("Ya existen ese nombre de usuario")
        
        return cd
        



class Aerolineaform(forms.Form):
    aerolinea = forms.CharField(max_length=20, label='Nombre aerolinea')


class Vueloform(forms.Form):
    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo')
    id_aerolinea = forms.ModelChoiceField(Aerolinea.objects.all())
    costo = forms.FloatField(label='Precio')


class Escalaform(forms.Form):
    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo',)
    postal_procedencia = forms.IntegerField(label='Codigo postal procedencia')
    postal_destino = forms.IntegerField(label='Codigo postal destino')
    fecha_salida = forms.DateField(label='Fecha de salida')
    fecha_llegada = forms.DateField(label='Fecha de llegada')
    requisitos = forms.CharField(widget=forms.Textarea, label='Requisitos')


