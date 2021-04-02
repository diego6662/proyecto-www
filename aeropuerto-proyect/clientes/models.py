from django.db import models
from django.contrib.auth.models import User
from vuelos.models import  Vuelo 

    
class Cliente(models.Model):
    cc = models.IntegerField(primary_key=True)
    vuelos_disponibles = models.IntegerField(null=False,blank=False)
    usuario_dj = models.ForeignKey(User,on_delete=models.CASCADE, null = False, blank=False)


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False,blank=False)
    Vuelo = models.ForeignKey(Vuelo,on_delete=models.CASCADE,null=False,blank=False)

