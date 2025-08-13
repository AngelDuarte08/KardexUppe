// Ver contraseña
  document.getElementById("verClave").addEventListener("change", function () {
    const passwordField = document.getElementById("password");
    passwordField.type = this.checked ? "text" : "password";
  });

  // Redirigir al calendario
  document.getElementById("btnCalendario").addEventListener("click", function () {
    window.location.href = "{{ url_for('auth_bp.calendar') }}";
  });