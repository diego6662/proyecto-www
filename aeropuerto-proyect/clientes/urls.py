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
]
