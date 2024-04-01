from django.contrib import admin
from .models import Usuario, Rol, Cliente, Historial, Citas, Estado, TipoPago, Factura, Servicio, Venta 

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Cliente)
admin.site.register(Historial)
admin.site.register(Citas)
admin.site.register(Estado)
admin.site.register(TipoPago)
admin.site.register(Factura)
admin.site.register(Servicio)
admin.site.register(Venta)
