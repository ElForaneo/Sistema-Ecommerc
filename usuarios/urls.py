from django.urls import path
from . import views

urlpatterns = [
    path('',views.PaginaLogin,name="login"),
    path('logout_user',views.logout_user,name="logout"),

    path('Dashboard/Usuario/',views.usuario,name="usuario"),
    path('Dashboard/Usuario/Registrar',views.PaginaRegistrar ,name="registrar"),
    path('Dashboard/Usuario/Editar_Usuario/<str:pk>/',views.EditarUsuario ,name="editar_usuario"),
    path('Dashboard/Usuario/Borrar_Usuario/<str:pk>/',views.BorrarUsuario ,name="borrar_usuario"),

]