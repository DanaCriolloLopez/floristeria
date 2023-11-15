"""
URL configuration for floristeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', views.ProductoListView.as_view(), name='producto-list'),
    path('producto/<int:pk>/detail/',
        views.ProductoDetailView.as_view(), name='producto-detail'),
    path('cliente/', views.ClienteListView.as_view(), name='cliente-list'),

    # Update
    path('producto/<int:pk>/update/',views.ProductoUpdate.as_view(),name='producto-update'), 
    #Create
    path('factura/create/', views.FacturaCreate.as_view(), name='factura-create'),

]