from django.urls import path
from . import views

urlpatterns = [
    path('Lista_Caja',views.Caja_lista,name="caja_lista"),
]