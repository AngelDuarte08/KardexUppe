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

function generateInstitutionalEmail() {
  const name = document.getElementById("names").value.trim().toLowerCase();
  const lastname1 = document.getElementById("lastname1").value.trim().toLowerCase();
  const lastname2 = document.getElementById("lastname2").value.trim().toLowerCase();
  const tipo = document.getElementById("role").value.trim().toLowerCase(); // toma el valor del select

  if (!name || !lastname1 || !lastname2 || !tipo) {
    alert("Por favor completa nombre, apellidos y rol.");
    return;
  }

  const initials = name.split(" ").map(word => word[0]).join("");
  let localPart = `${initials}.${lastname1}${lastname2}`;
  let domain = "uppenjamo.edu.mx";

  if (tipo === "docente") {
    localPart = `doc.${localPart}`;
    domain = "docentes.uppenjamo.edu.mx";
  } else if (tipo === "administrador") {
    localPart = `admin.${localPart}`;
    domain = "admin.uppenjamo.edu.mx";
  }

  const correo = `${localPart}@${domain}`;
  document.getElementById("emailInput").value = correo;
}

