$(document).ready(function() {
    $("#enviar").click(function(event) {
      var nombre = $("#nombre").val();
      if (nombre.length < 3 || nombre.length > 20) {
        event.preventDefault();
        $("#nombre-error").text("El nombre debe tener entre 3 y 20 caracteres.");
      }
    });
  });