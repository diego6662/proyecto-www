from django.db import models
from django.contrib.auth.models import User
from vuelos.models import  Vuelo 

    
class Cliente(models.Model):
    cc = models.IntegerField(primary_key=True, verbose_name="cedula")
    vuelos_disponibles = models.IntegerField(null=False,blank=False, verbose_name="numero de reservas")
    usuario_dj = models.ForeignKey(User,on_delete=models.CASCADE, null = False, blank=False,verbose_name="usuario")
    image_perfil = models.ImageField(upload_to='clientes/perfiles/',null = True, blank=True)
    def __str__(self):
        return str(self.cc)



class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False,blank=False, verbose_name="cliente")
    vuelo = models.ForeignKey(Vuelo,on_delete=models.CASCADE,null=False,blank=False, verbose_name="vuelo" )

    def __str__(self):
        return f'{self.cliente.cc} {self.vuelo.id_vuelo}' 

