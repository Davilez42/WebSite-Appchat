const loguin = () => {
  nombre = document.getElementById("floatingInput-username").value;
  contraseña = document.getElementById("floatingInput-password").value;

  if (nombre == "" && contraseña == "") {
     alert("por favor rellene todos los campos");
  } else {
    if (nombre == "") {
      alert("por favor rellene el nombre de usuario");
    } else if (contraseña == "") {
      alert("por favor rellene la contraseña de usuario");
    }
    else{
        document.form.submit();
    }
  }
};
