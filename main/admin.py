from django.contrib import admin
from .models import Car, Services, Auto_parts

admin.site.register(Car)
admin.site.register(Auto_parts)
admin.site.register(Services)
