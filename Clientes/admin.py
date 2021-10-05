from django.contrib import admin
from .models import Clientes

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Nombres', 
        'Apellidos', 
        'Direccion', 
        'Telefono',
        'Correo', 
        'Cedula',
        'Fecha_Nacimiento',

    )

    

admin.site.register(Clientes, ClientesAdmin)