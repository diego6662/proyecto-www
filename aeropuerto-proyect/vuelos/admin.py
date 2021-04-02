from django.contrib import admin
from .models import *
# Register your models here.

class AerolineaAdmin(admin.ModelAdmin):
    fields = ('nombre',)

class VueloAdmin(admin.ModelAdmin):
    fields = ('id_vuelo','aerolinea','costo')

class EscalaAdmin(admin.ModelAdmin):
    fields = ('vuelo','nombre_procedencia','cod_procedencia','nombre_destino','cod_destino','fecha_salida','fecha_llegada','requicitos')

admin.site.register(Aerolinea,AerolineaAdmin)
admin.site.register(Vuelo,VueloAdmin)
admin.site.register(Escala,EscalaAdmin)

