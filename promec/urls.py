"""
URL configuration for promec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from promecapp import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),    
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),    
    path('logout/', views.logout_view, name='logout'), 
    path('usuarios/', views.usuarios, name='usuarios'),
    path('clientes/', views.clientes, name='clientes'),
    path('historial/', views.historial, name='historial'),
    path('citas/', views.citas, name='citas'),
    path('ventas/', views.ventas, name='ventas'),
    path('servicios/', views.servicios, name='servicios'),
    path('facturas/', views.facturas, name='facturas'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_cita/', views.agregar_cita, name='agregar_cita'),
    path('agregar_factura/', views.agregar_factura, name='agregar_factura'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('agregar_venta/', views.agregar_venta, name='agregar_venta'),
    path('agregar_historial/', views.agregar_historial, name='agregar_historial'),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('editar_cita/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('editar_venta/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('editar_historial/<int:historial_id>/', views.editar_historial, name='editar_historial'),
    path('editar_servicio/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('editar_factura/<int:factura_id>/', views.editar_factura, name='editar_factura'),
    path('eliminar_venta/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    path('eliminar_servicio/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('eliminar_factura/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
    path('eliminar_historial/<int:historial_id>/', views.eliminar_historial, name='eliminar_historial'),
    path('registro/', views.registro, name='registro'),

]

handler404 = 'promecapp.views.error_404_view'
