from django.db import models
from django.contrib.auth.models import User

# MODELOS

class Aerolinea(models.Model):
    nombre = models.CharField(max_length=100) 

class Vuelo(models.Model):
    id_vuelo = models.CharField(max_length=30,primary_key=True)
    aerolinea = models.ForeignKey(Aerolinea,on_delete=models.CASCADE)
    costo = models.FloatField(blank=False,null=False)

class Escala(models.Model):
    vuelo = models.ForeignKey(Vuelo,on_delete=models.CASCADE)
    nombre_procedencia = models.CharField(max_length=30,null=False,blank=False)
    cod_procedencia = models.IntegerField(null=False,blank=False)
    nombre_destino = models.CharField(max_length=30,null=False,blank=False)
    cod_destino = models.IntegerField(null=False,blank=False)
    fecha_salida = models.DateTimeField(null=False,blank=False)
    fecha_llegada = models.DateTimeField(null=False,blank=False)
    requicitos = models.TextField(null=False,blank=False)


