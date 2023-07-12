from django.contrib import admin
from .models import Producto, Carrito, Compra


admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Compra)

