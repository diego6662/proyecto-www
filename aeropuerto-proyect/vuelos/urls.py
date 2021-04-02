from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'vuelos'
urlpatterns = [
    path('', views.index, name='index'),
    path('vuelo', views.vuelo, name='vuelo'),
    path('login', views.login, name='login'),
    path('registrar-aerolinea', views.registrar_aerolinea, name='registrar-aerolinea'),

]


