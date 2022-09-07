from pathlib import Path
from django.urls import path

from . import views

urlpatterns =[
    path('Entradas/',views.entradas,name="entradas"),
    path('Entradas/RegistrarCodigoBarras',views.Crearentradas,name="crear_entrada"),
    path('Entradas/RegistrarProducto',views.Crearproducto,name="crear_producto"),
    path('Entradas/Editar_Producto/<str:pk>',views.EditarProducto,name="editar_producto"),
    path('Entradas/Borrar_Producto/<str:pk>',views.BorrarProducto,name="borrar_producto"),
]