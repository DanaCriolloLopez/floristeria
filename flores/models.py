from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Producto(models.Model):
    """ Productos en stock """
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    cantidad = models.IntegerField(max_length=5)
    precio = models.IntegerField(max_length=10)
    imagen = models.ImageField(upload_to='flores/')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    """ Clientes """
    cedula = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.cedula + " " + self.nombre

class Factura(models.Model):
    """ Facturación """
    codigo = models.CharField(max_length=6)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT,related_name='get_cliente' )
    cantidad = models.IntegerField(max_length=5)
    producto = models.ForeignKey('Producto', on_delete=models.PROTECT,related_name='get_producto')
    total = models.IntegerField(max_length=10)
    
    def __str__(self):
        return self.codigo 
    
    def get_absolute_url(self):
        return reverse('producto-list')
