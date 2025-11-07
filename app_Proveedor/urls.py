# app_Proveedor/urls.py (Versión Corregida)

from django.urls import path
from . import views

urlpatterns = [
    # 1. La ruta raíz ahora mostrará la lista de proveedores por defecto
    path('', views.inicio_proveedor, name='ver_proveedores'), 

    # 2. La ruta 'inicio' ahora usa la vista simple 'inicio_sistema'
    path('inicio/', views.inicio_sistema, name='inicio'), 
    
    # CRUD Proveedor
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/guardar_actualizacion/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),
]