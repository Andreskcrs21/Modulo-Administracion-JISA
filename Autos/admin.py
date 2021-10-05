from django.contrib import admin
from .models import Auto

# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Marca',
        'Modelo', 
        'Año', 
        'Color', 
        'Placa',
        'Cilindrada', 
        'Transmision', 
        'Precio', 
        'Foto',

    )

admin.site.register(Auto, AutoAdmin)