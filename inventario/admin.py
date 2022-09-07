from django.contrib import admin
from .models import Almacenes, AlmacenAdmin

# Register your models here.

admin.site.register(Almacenes,AlmacenAdmin)