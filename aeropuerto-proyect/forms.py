from django import forms

class Loginform(forms.Form):
    usuario = forms.CharField(max_length=20,label='Nombre de usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput(),
            label='Contraseña')


class Aerolineaform(forms.Form):
    aerolinea = forms.CharField(max_length=20, label='Nombre aerolinea')


class Vueloform(forms.Form):
    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo')
    id_aerolinea = forms.CharField(max_length=30, label='Codigo de la aerolinea')
    costo = forms.FloatField(label='Precio')


class Escalaform(forms.Form):
    id_vuelo = forms.CharField(max_length=30, label='Codigo del vuelo')
    postal_procedencia = forms.IntegerField(label='Codigo postal procedencia')
    postal_destino = forms.IntegerField(label='Codigo postal destino')
    fecha_salida = forms.DateField(label='Fecha de salida')
    fecha_llegada = forms.DateField(label='Fecha de llegada')
    requisitos = forms.CharField(widget=forms.Textarea, label='Requisitos')
