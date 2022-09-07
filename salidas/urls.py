from django.urls import path
from . import views

urlpatterns = [
    path('Salidas/',views.salidas_lista,name="salida"),
    path('Salidas/Registrar',views.salidas_add, name='salida_add'),
]