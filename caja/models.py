from enum import auto
from django.db import models
from usuarios.models import Users
from restaurante.models import Platillos

# Create your models here.

class orden(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    usuario = models.ForeignKey(Users,null=False,blank=True,default=False , on_delete=models.DO_NOTHING)
    platillos = models.ForeignKey(Platillos,null=True,on_delete=models.DO_NOTHING)
    fecha_creada = models.DateTimeField(verbose_name='Orden creada',auto_now_add=True)
    orden_actualizada = models.DateTimeField(verbose_name='Orden actulizada', auto_now=True)

class cortecaja(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    usuario = models.ForeignKey(Users,null=False,blank=True, default=False , on_delete=models.DO_NOTHING)
    platillos = models.ForeignKey(Platillos,null=True,on_delete=models.DO_NOTHING)
    Nd_caja = models.CharField(max_length=5,blank=True,null=False)

    MontoInicial = models.CharField(max_length=200,blank=True,null=False)
    MontoDCierre = models.CharField(max_length=200,blank=True,null=False)

    Fecha_apertura = models.DateField(auto_now=True)
    Hora_apertura = models.TimeField(auto_now=True)
    Fecha_cierre = models.DateField(auto_now=True)
    Hora_cierre = models.TimeField(auto_now=True)
    fecha_creada = models.DateTimeField(verbose_name='Orden creada',auto_now_add=True)
    corte_actualizado = models.DateTimeField(verbose_name='Orden actulizada', auto_now=True)