<form action="../controlador/control_principal.php" method="post"> <!-- Especifica dónde se deben enviar los datos del formulario cuando se envía. -->
    <label for="nombre"><strong>Nombre:</strong><br></label>
    <input type="text" id="nombre" name="nombre" required><br>

    <label for="apellido"><strong>Apellido:</strong><br></label>
    <input type="text" id="apellido" name="apellido" required><br>

    <br><input type="submit" value="Enviar">
</form>