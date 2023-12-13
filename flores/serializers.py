from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
        
        
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'