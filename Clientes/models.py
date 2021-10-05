from django.db import models

# Create your models here.
class Clientes(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Correo = models.EmailField()
    Cedula = models.CharField(max_length=10)
    Fecha_Nacimiento = models.DateField(help_text="Ejemplo: 08/04/1999" , max_length=10)
