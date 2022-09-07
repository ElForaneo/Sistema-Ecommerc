from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Calenadrio/',views.calendario,name="calendario"),
]
