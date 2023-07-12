const botonesComprar = document.querySelectorAll('.btn-comprar');
const carritoItems = document.getElementById('carrito-items');
const carritoTotal = document.getElementById('carrito-total');
let carrito = [];

botonesComprar.forEach(boton => {
  boton.addEventListener('click', () => {
    const productoId = boton.dataset.producto;
    const cantidadInput = document.getElementById(`cantidad-${productoId}`);
    const cantidad = parseInt(cantidadInput.value);
    const producto = {
      id: productoId,
      nombre: boton.parentNode.parentNode.querySelector('.nombre').textContent,
      foto: boton.parentNode.parentNode.querySelector('img').src,
      cantidad: cantidad,
      precio: parseFloat(boton.parentNode.parentNode.querySelector('.precio').textContent.replace('Precio: $', '')),
    };

    agregarAlCarrito(producto);
    cantidadInput.value = '1';
  });
});

function agregarAlCarrito(producto) {
  const itemExistente = carrito.find(item => item.id === producto.id);

  if (itemExistente) {
    itemExistente.cantidad += producto.cantidad;
  } else {
    carrito.push(producto);
  }

  mostrarCarrito();
}

function mostrarCarrito() {
  carritoItems.innerHTML = '';
  let total = 0;

  carrito.forEach(item => {
    const itemCarrito = document.createElement('div');
    itemCarrito.classList.add('item-carrito');

    const imagen = document.createElement('img');
    imagen.src = item.foto;
    imagen.alt = item.nombre;
    imagen.classList.add('item-imagen');

    const nombre = document.createElement('p');
    nombre.textContent = item.nombre;
    nombre.classList.add('item-nombre');

    const cantidad = document.createElement('p');
    cantidad.textContent = `Cantidad: ${item.cantidad}`;
    cantidad.classList.add('item-cantidad');

    const eliminar = document.createElement('span');
    eliminar.classList.add('btn-eliminar');
    eliminar.innerHTML = '<i class="fa-solid fa-trash"></i>';
    eliminar.addEventListener('click', eliminarItemCarrito);

    itemCarrito.appendChild(imagen);
    itemCarrito.appendChild(nombre);
    itemCarrito.appendChild(cantidad);
    itemCarrito.appendChild(eliminar);
    carritoItems.appendChild(itemCarrito);

    total += item.precio * item.cantidad;
  });

  carritoTotal.textContent = `Total: $${total.toFixed(2)}`;
}


var botonesEliminarItem=document.getElementsByClassName('btn-eliminar');
    for(var i=0; i < botonesEliminarItem.length;i++){
        var button = botonesEliminarItem[i];
        button.addEventListener('click', eliminarItemCarrito);
    }
function eliminarItemCarrito(event){
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();

    actualizarTotalCarrito();

    ocultarCarrito();
}
