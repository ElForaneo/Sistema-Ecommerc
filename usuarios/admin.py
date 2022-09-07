from django.contrib import admin
from .models import Users, UsersAdmin
# Register your models here.

admin.site.register(Users,UsersAdmin)