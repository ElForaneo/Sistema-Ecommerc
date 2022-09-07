from django.contrib import admin
from .models import Platillos, PlatillosAdmin
from .models import locales, LocalesAdmin


# Register your models here.

admin.site.register(Platillos, PlatillosAdmin)
admin.site.register(locales,LocalesAdmin)
