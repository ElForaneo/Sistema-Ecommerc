from django.urls import path
from . import views


urlpatterns = [
    path('Restaurante/',views.restaurante,name="restaurante"),
    path('Restaurante/Crear_Platillos',views.crearplatillos, name="crearplat"),
    path('Restaurante/Crear_Locales',views.crearlocal, name="crearlocales")
]