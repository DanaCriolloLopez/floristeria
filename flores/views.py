from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from flores.models import *

# Create your views here.
#Vistas genericas de django 

class ProductoListView(ListView):
    #obligatorio poner el modelo con el que va a ineractuar 
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

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
