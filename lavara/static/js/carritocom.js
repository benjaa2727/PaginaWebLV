// Función para calcular el total y actualizar el campo de total
function calcularTotal() {
    var total = 0;
    var precios = document.getElementsByClassName("precio");
    var cantidades = document.getElementsByClassName("cantidad");

    for (var i = 0; i < precios.length; i++) {
        total += parseFloat(precios[i].innerHTML) * parseInt(cantidades[i].value);
    }

    document.getElementById("total").innerHTML = total.toFixed(2);
}

// Función para restar el stock de un producto
function restarStock(productoId) {
    var stock = document.getElementById("stock_" + productoId).innerHTML;
    var cantidad = document.getElementById("cantidad_" + productoId).value;

    if (parseInt(cantidad) > parseInt(stock)) {
        alert("No hay suficiente stock disponible.");
        document.getElementById("cantidad_" + productoId).value = stock;
        return;
    }

    document.getElementById("stock_" + productoId).innerHTML = parseInt(stock) - parseInt(cantidad);
}

// Función para agregar un producto al carrito
function agregarProducto(nombre, precio, imagen) {
    var carrito = document.getElementById("carrito");
    var fila = document.createElement("tr");

    fila.innerHTML = `
        <td><img src="${imagen}" alt="${nombre}" width="50"></td>
        <td>${nombre}</td>
        <td class="precio">${precio}</td>
        <td><input type="number" class="cantidad" id="cantidad_${nombre}" value="1" onchange="calcularTotal(); restarStock('${nombre}');"></td>
    `;

    carrito.appendChild(fila);
    calcularTotal();
    restarStock(nombre);
}

// Función para realizar el pago
function pagar() {
    // Aquí puedes agregar la lógica para procesar el pago
    alert("¡Pago realizado con éxito!");
    location.reload();
}