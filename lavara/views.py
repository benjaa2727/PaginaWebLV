from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, Compra
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import ProductoForm


@login_required
def mostrar_productos(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    data = {
        'productos': [
            {
                'id': producto.id,
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'precio': producto.precio,
                'stock': producto.stock,
                'foto': producto.foto.url
            }
            for producto in productos
        ],
        'form': form.as_p()
    }
    return JsonResponse(data)





@login_required(login_url='login')
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        carrito.agregar_producto(producto)

        return redirect('carrito')

    return render(request, 'detalle_producto.html', {'producto': producto})


@login_required(login_url='login')
def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.itemcarrito_set.all()
    total = carrito.obtener_precio_total()
    username = request.user.username
    return render(request, 'carrito.html', {'carrito': carrito, 'items': items, 'total': total,'username': username })


@login_required(login_url='login')
def eliminar_producto(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    producto = get_object_or_404(Producto, pk=producto_id)

    carrito.eliminar_producto(producto)

    return redirect('carrito')


@login_required(login_url='login')
def agregar_carrito(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        producto_id = request.POST.get('producto_id')
        cantidad = request.POST.get('cantidad')

        producto = get_object_or_404(Producto, pk=producto_id)
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        carrito.agregar_producto(producto, int(cantidad))

        return JsonResponse({'message': 'Producto agregado al carrito'})

    return JsonResponse({'error': 'Error al procesar la solicitud'})


@login_required(login_url='login')
def pagar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)

    for item in carrito.itemcarrito_set.all():
        producto = item.producto
        cantidad = item.cantidad
        
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            producto.save()
            
            compra = Compra.objects.create(usuario=request.user, producto=producto, cantidad=cantidad)
            compra.save()

    carrito.itemcarrito_set.all().delete()
    
    return redirect('home')


@login_required(login_url='login')
def mis_productos(request):
    productos = Producto.objects.all()
    username = request.user.username
    return render(request, 'productos.html', {'productos': productos, 'username': username})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo nuevamente.')
    return render(request, 'login.html')







@login_required(login_url='login')
def contactenos(request):
    username = request.user.username
    return render(request, "Contactenos.html", {'username': username})


@login_required(login_url='login')
def ers(request):
    username = request.user.username
    return render(request, "ers.html", {'username': username})





@login_required(login_url='login')
def quienessomos(request):
    username = request.user.username
    return render(request, "quienessomos.html", {'username': username})


@login_required(login_url='login')
def home_view(request):
    username = request.user.username
    return render(request, 'index.html', {'username': username})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')