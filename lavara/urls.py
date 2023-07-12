
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import contactenos, ers, login_view, logout_view, detalle_producto, carrito, eliminar_producto, agregar_carrito
from . views import quienessomos, home_view
from .views import  mis_productos, pagar_carrito, mostrar_productos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name = 'login'),
    path('contactenos/',contactenos, name = 'contactenos' ),
    path('ers/',ers, name = 'ers' ),
    path('home/', home_view, name = 'home'),
    path('misproductos/', mis_productos, name = 'misproductos'),
    path('quienessomos/', quienessomos, name = 'quienessomos'),
    path('logout/',logout_view, name = 'logout'),
    

    path('productos/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('carrito/', carrito, name='carrito'),
    path('carrito/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('agregar-carrito/', agregar_carrito, name='agregar_carrito'),
    path('pagar-carrito/', pagar_carrito, name='pagar_carrito'),


    path('mostrar_productos/', mostrar_productos, name='mostrar_productos'),


   
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
