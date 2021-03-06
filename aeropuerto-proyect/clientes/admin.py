from django.contrib import admin
from .models import Cliente, Reserva
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    fields = ('cc','vuelos_disponibles','usuario_dj','image_perfil')
    list_display=("cc","vuelos_disponibles","usuario_dj",)

class ReservaAdmin(admin.ModelAdmin):
    fields = ('cliente','vuelo')


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Reserva)
