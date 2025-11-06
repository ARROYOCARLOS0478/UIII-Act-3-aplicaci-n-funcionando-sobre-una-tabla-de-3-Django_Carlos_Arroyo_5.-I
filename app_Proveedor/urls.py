# app_Proveedor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Inicio del sistema (muestra la página de información)
    path('', views.inicio_proveedor, name='ver_proveedores'), 
    path('inicio/', views.inicio_proveedor, name='inicio'), # Ruta que usa la navbar

    # CRUD Proveedor
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    # 'ver_proveedores' ya está mapeado al path('') y muestra la lista de proveedores
    path('proveedor/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/guardar_actualizacion/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),
]