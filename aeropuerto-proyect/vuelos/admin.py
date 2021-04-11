from django.contrib import admin
from .models import *
# Register your models here.


class AerolineaAdmin(admin.ModelAdmin):
    #fields = ('nombre',)
    readonly_fields = ['id']
    fields = ['id','nombre']
class VueloAdmin(admin.ModelAdmin):
    fields = ['id_vuelo','aerolinea','destino','costo','fecha']

class EscalaAdmin(admin.ModelAdmin):
    fields = ('vuelo','nombre_procedencia','cod_procedencia','nombre_destino','cod_destino','fecha_salida','fecha_llegada','requisitos')

admin.site.register(Aerolinea,AerolineaAdmin)
admin.site.register(Vuelo,VueloAdmin)
admin.site.register(Escala,EscalaAdmin)
admin.site.register(Ciudades,)

