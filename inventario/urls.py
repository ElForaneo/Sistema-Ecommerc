from django.urls import path
from . import views


urlpatterns = [
    path('Inventario', views.inventario, name="inventario"),
]
