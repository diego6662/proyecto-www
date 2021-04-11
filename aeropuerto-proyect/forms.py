from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError 

from vuelos.models import Aerolinea, Ciudades


# -*- coding:utf-8 -*-
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

class Loginform(forms.Form):
    usuario = forms.CharField(max_length=20,label='Nombre de usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput(),
            label='Contraseña')


class RegistroClienteform(forms.Form):
    # CSS ERRORS
    error_css_class = 'invalid-feedback'
    required_css_class = 'required'
    error_css_class = "error"
 
    # COMPONENETES 
    cc = forms.IntegerField(required=True,label='Identificacion',help_text="Debe contener al menos 7 digitos" )
    nombre = forms.CharField(max_length=20,required=True, label='Nombre')
    apellido = forms.CharField(max_length=20,required=True, label='Apellido')
    username = forms.CharField(max_length=20,required=True )
    email = forms.EmailField(max_length=30,required=True ,label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(),label="Contraseña", help_text="Debe contener al menos 8 caracteres, un caracter especial y una mayusculo")
    password2 = forms.CharField(widget=forms.PasswordInput(),label="Confirmar Contraseña", help_text ="La contraseña de nuevo")

    # CAMBIOS EN EL CSS
    cc.widget.attrs.update({'class': 'form-control'})  
    nombre.widget.attrs.update({'class': 'form-control'})  
    apellido.widget.attrs.update({'class': 'form-control'})  
    username.widget.attrs.update({'class': 'form-control'}) 
    email.widget.attrs.update({'class': 'form-control'}) 
    password1.widget.attrs.update({'class': 'form-control'})  
    password2.widget.attrs.update({'class': 'form-control'})  

    def clean_password2(self):
        psswrd1 = self.cleaned_data.get("password1")
        psswrd2 = self.cleaned_data.get("password2")
        
        if not(psswrd1 and psswrd2):
            raise ValidationError("Los campos son obligatorios")
        elif psswrd1 != psswrd2:
            raise ValidationError("Las contraseñas no coinciden")
        elif len(psswrd1) < 8:
            raise ValidationError("La contraseñas debe tener almenos 8 caracteres")
        elif len(psswrd1) > 20:
            raise ValidationError("La contraseñas debe tener maximo 20 caracteres")
        elif psswrd1.isalpha():
            raise ValidationError("La contraseñas debe tener al menos un caracter especial")
        elif psswrd1.lower() == psswrd1:
            raise ValidationError("La contraseña debe tneer al menos una mayuscula")
        return psswrd2

    def clean_cc(self):
        cc = self.cleaned_data.get("cc")
        if len(str(cc)) < 7:
            raise ValidationError("La Identificacion no es valida")
        return cc

    def clean_username(self):
        newusername = self.cleaned_data.get("username")
        number_usrs = User.objects.filter(username=newusername).count()
        if number_usrs > 0:
            raise ValidationError("Este nombre de usuario ya se encuentra en uso")
        return newusername

    def as_div(self):
        output = []
        
        for boundfield in self: #see original Form class __iter__ method
            row_template = u'''
            <div class=" mb-3 %(div_class)s">
                %(label)s
                <div class="input %(input_class)s">
                    %(field)s
                    <span class="help-block">%(help_text)s </span>
                </div>
                <div class="invalid-feedback">%(error_l)s </div>
            </div>
            '''
            row_dict = {
                "input_class" : "",
                "div_class" : "",
                "required_label" : "",
                "field" : boundfield.as_widget(),
                "label" : boundfield.label_tag(),
                "help_text" : boundfield.help_text,
                "error_l" : "",
            }

            
            if boundfield.errors:
                row_dict["error_l"]  = '''<div class="alert alert-danger" role="alert">''' + str(boundfield.errors )+ '''
                                        </div>'''

            output.append(row_template % row_dict)
        return mark_safe(u'\n'.join(output))

"""
    def clean(self):
        cd = self.cleaned_data
        # {'cc': 12345, 'username': 'asdf', 'email': 'qefasdf@gmail.com', 'password1': '1234', 'password2': '12346'}
        psswrd1 = cd.get("password1")
        psswrd2 = cd.get("password2")
        new_username = cd.get("username")
        cc = cd.get("cc")
        number_usrs = User.objects.filter(username=new_username)
        
        print("VALIDATION OF DATA-----------_>",cd)
        if psswrd1 != psswrd2:
            raise ValidationError("Las contraseñas no coinciden")
        elif len(psswrd1) < 8:
            raise ValidationError("La contraseñas debe tener almenos 8 caracteres")
        elif len(psswrd1) > 20:
            raise ValidationError("La contraseñas debe tener maximo 20 caracteres")
        elif psswrd1.isalpha():
            raise ValidationError("La contraseñas debe tener al menos un caracter especial")
        elif psswrd1.lower() == psswrd1:
            raise ValidationError("La contraseña debe tneer al menos una mayuscula")
        elif len(cc) < 8:
            raise ValidationError("La Identificacion no es valida")
        elif number_usrs > 0:
            raise ValidationError("Este nombre de usuario ya se encuentra en uso")
        
        return cd
"""
"""
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
        
"""

class Aerolineaform(forms.Form):
    aerolinea = forms.CharField(max_length=20, label='Nombre aerolinea')


class Vueloform(forms.Form):
    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo')
    id_aerolinea = forms.ModelChoiceField(Aerolinea.objects.all())
    destino = forms.CharField(max_length=30,label='Destino')
    costo = forms.FloatField(label='Precio')
    fecha_vuelo = forms.DateField(label='Fecha de vuelo')

class Escalaform(forms.Form):
#    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo',)
    procedencia = forms.CharField(max_length=30, label='Ciudad de procedencia')
    postal_procedencia = forms.IntegerField(label='Codigo postal procedencia')
    destino = forms.CharField(max_length=30, label='Ciudad de destino')
    postal_destino = forms.IntegerField(label='Codigo postal destino')
    fecha_salida = forms.DateField(label='Fecha de salida', widget = forms.SelectDateWidget(years=[2021],months={4:'Abril'},))
    fecha_llegada = forms.DateField(label='Fecha de llegada', widget = forms.SelectDateWidget(years=[2021],months={4:'Abril'}))
    requisitos = forms.CharField(widget=forms.Textarea, label='Requisitos')


class CiudadForm(forms.Form):
    postal = forms.IntegerField(label = 'Codigo postal')
    nombre = forms.CharField(max_length=30,label='Nombre de la ciudad')
    foto = forms.ImageField(label='Foto de la ciudad')
