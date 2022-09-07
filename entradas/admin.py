from django.contrib import admin
from .models import GenerarCodigoBarras,BarcodeAdmin
from .models import Inventario, EntradaAdmin
from .models import categoria

# Register your models here.

admin.site.register(GenerarCodigoBarras,BarcodeAdmin)
admin.site.register(Inventario,EntradaAdmin)
admin.site.register(categoria)