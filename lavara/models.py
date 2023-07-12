from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='productos/')

    def str(self):
        return self.nombre
    


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)



    def agregar_producto(self, producto, cantidad):
        item_carrito = ItemCarrito.objects.filter(carrito=self, producto=producto).first()

        if item_carrito:
            item_carrito.cantidad += cantidad  
            item_carrito.save()
        else:
            item_carrito = ItemCarrito(carrito=self, producto=producto, cantidad=cantidad)
            item_carrito.save()


    def eliminar_producto(self, producto):
        item_carrito = ItemCarrito.objects.filter(carrito=self, producto=producto).first()
        if item_carrito:
            item_carrito.delete()


    def obtener_precio_total(self):
        items = ItemCarrito.objects.filter(carrito=self)
        total = sum(item.obtener_subtotal() for item in items)
        return total


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)



class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def obtener_precio_unitario(self):
        return self.producto.precio
    
    def obtener_subtotal(self):
        subtotal = self.cantidad * self.producto.precio
        return subtotal