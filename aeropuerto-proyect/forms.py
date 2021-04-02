from django import forms

class Loginform(forms.Form):
    usuario = forms.CharField(max_length=20,label='Nombre de usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput(),
            label='Contraseña')
