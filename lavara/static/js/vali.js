document.addEventListener("DOMContentLoaded", function() {
    var emailInput = document.getElementById('email');
    var errorMessage = document.getElementById('email-error');
  
    function validateEmail(email) {
      return email.length >= 5 && email.includes('@');
    }
  
    function handleSubmit(event) {
      event.preventDefault();
  
      var email = emailInput.value.trim();
  
      if (validateEmail(email)) {
        errorMessage.style.display = 'none';
        event.target.submit();
      } else {
        errorMessage.style.display = 'block';
        errorMessage.innerHTML = 'Correo electrónico inválido';
      }
    }
  
    document.getElementById('contact-form').addEventListener('submit', handleSubmit);
  });