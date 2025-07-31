function generatePassword() {
  const prefix = "UPPE";
  const suffix = "P";
  const middleLength = 6;
  const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let middle = "";

  for (let i = 0; i < middleLength; i++) {
    middle += characters.charAt(Math.floor(Math.random() * characters.length));
  }

  const password = prefix + middle + suffix;
  document.getElementById("passwordInput").value = password;
}

function generateEmail() {
    const name = document.getElementById("names").value.trim().toLowerCase();
    const lastname1 = document.getElementById("lastname1").value.trim().toLowerCase();
    const lastname2 = document.getElementById("lastname2").value.trim().toLowerCase();
    
    if (!name || !lastname1 || !lastname2) {
      alert("Por favor llena nombre y apellidos para generar el correo.");
      return;
    }

    const initials = name.split(" ").map(word => word[0]).join(""); // Ej: Luis Angel → "la"
    const correo = `${initials}.${lastname1}${lastname2}@uppenjamo.edu.mx`;

    document.getElementById("emailInput").value = correo;
  }