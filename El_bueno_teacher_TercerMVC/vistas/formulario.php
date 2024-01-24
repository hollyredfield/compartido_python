<form action="../controlador/controlador_principal.php" method="post">
    <input type="text" name="accion" value="grabar" hidden>
    <label for="nombre:">Nombre:</label>
    <input type="text" name="nombre" required><br>
    <label for="apellidos">Apellidos:</label>
    <input type="text" name="apellidos" required><br>
    <input type="submit" value="Enviar">
</form>