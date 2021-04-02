from django.db import models
from django.contrib.auth.models import User

# MODELOS

class Aerolinea(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="nombre")
    
    def __str__(self):
        return nombre


class Vuelo(models.Model):
    id_vuelo = models.CharField(max_length=30,primary_key=True, verbose_name="id_vuelo")
    aerolinea = models.ForeignKey(Aerolinea,on_delete=models.CASCADE, verbose_name="aerolinea")
    costo = models.FloatField(blank=False,null=False, verbose_name="costo")

    def __str__(self):
        return str(id_vuelo)


class Escala(models.Model):
    vuelo = models.ForeignKey(Vuelo,on_delete=models.CASCADE)
    nombre_procedencia = models.CharField(max_length=30,null=False,blank=False)
    cod_procedencia = models.IntegerField(null=False,blank=False)
    nombre_destino = models.CharField(max_length=30,null=False,blank=False)
    cod_destino = models.IntegerField(null=False,blank=False)
    fecha_salida = models.DateTimeField(null=False,blank=False)
    fecha_llegada = models.DateTimeField(null=False,blank=False)
    requicitos = models.TextField(null=False,blank=False)

    def __str__(self):
        return str(vuelo) +"," +  str(nombre_procedencia) 

