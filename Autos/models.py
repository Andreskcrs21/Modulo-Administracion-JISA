from django.db import models
from django.db.models.base import Model

# Create your models here.
transmision = (('Manual', 'Manual'), ('Automatico', 'Automatico'))

class Auto(models.Model):
    Marca = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Año = models.IntegerField(max_length=4)
    Color = models.CharField(max_length=30)
    Placa = models.CharField(max_length=15)
    Cilindrada = models.IntegerField(max_length=10)
    Transmision = models.CharField(max_length=30, choices=transmision)
    Precio = models.DecimalField(max_digits=20, decimal_places=2)
    Foto = models.ImageField(upload_to='fotos')

class Moto(models.Model):
    Marca = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Año = models.IntegerField(max_length=4)
    Color = models.CharField(max_length=30)
    Placa = models.CharField(max_length=15)
    Cilindrada = models.IntegerField(max_length=10)
    Precio = models.DecimalField(max_digits=20, decimal_places=2)
    Foto = models.ImageField(upload_to='fotos')
    