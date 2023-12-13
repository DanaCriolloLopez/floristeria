from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from flores.models import *
from .serializers import *
from rest_framework import viewsets

# Create your views api.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
 
 
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer



# Create your views here.
#Vistas genericas de django 

class ProductoListView(ListView):
    #obligatorio poner el modelo con el que va a ineractuar 
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'

class ClienteListView(ListView):
    model = Cliente

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__' 

class FacturaCreate(CreateView):
    model = Factura
    fields = '__all__'

class FacturaListView(ListView): 
    model = Factura
    fields = '__all__'
    
    