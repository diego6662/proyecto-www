from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'vuelos'
urlpatterns = [
    path('', views.index, name='index'),
    path('vuelo/', views.vuelo, name='vuelo'),
    path('registrar-aerolinea/', views.registrar_aerolinea, name='registrar-aerolinea'),
    path('registrar-vuelo/', views.registrar_vuelo, name='registrar-vuelo'),
    path('registrar-escala-<str:id>', views.registrar_escala, name='registrar-escala'),
    path('modificar-aerolinea-<int:id>', views.modificar_aerolinea, name='modificar-aero'),
    path('vuelo-<str:id>', views.vista_vuelo, name='vista-vuelo'),
    path('admin-vuelo-<str:id>', views.vuelo_admin, name='vuelo-admin'),
    path('eliminar-vuelo-<str:id>', views.eliminar_vuelo, name='eliminar-vuelo'),
    path('editar-vuelo-<str:id>', views.editar_vuelo, name='editar-vuelo'),

]


