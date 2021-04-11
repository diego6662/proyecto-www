from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'clientes'
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.registrar_usuario, name='signup'),
    path('perfil', views.perfil, name='perfil'),
    path('reserva-<str:vuelo>', views.reserva, name='reserva'),
    path('usuarioAdmin/', views.usuarios_admin, name='usuarios_admin'),
    path('clienteAdmin-<int:cliente_id>/', views.cliente_perfil_admin, name='clientePerfilAdmin'),
    path('eliminarCliente-<int:cliente_id>/', views.eliminar_cliente, name='eliminarCliente'),
    path('cancelar-reserva-<int:id>', views.cancelar_reserva, name='cancelar_reserva'),
    path('editar-perfil', views.editar_perfil, name='editar_perfil'),
]
