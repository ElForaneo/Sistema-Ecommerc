from contextlib import nullcontext
from django.db import models
from django.contrib import admin
from restaurante.models import locales
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MiUserMananger(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError("Los Usuarios necestian un nombre")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(
            password=password,
            username=username,
            email = self.normalize_email(email),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user


class Users(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email",max_length=60, unique=True)
    username = models.CharField(max_length=30,unique=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=16,unique=True,null=True)
    local = models.ForeignKey(locales,null=True ,on_delete=models.DO_NOTHING)
    date_creado = models.DateTimeField(verbose_name='Fecha creado',auto_now_add=True)
    date_login = models.DateTimeField(verbose_name='Ultimo Login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MiUserMananger()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def nombre_completo(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre_completo','telefono','is_admin','is_staff','is_superuser')