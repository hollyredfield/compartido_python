<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") { //  Si el método de solicitud del servidor es POST entonces
        $nombre = $_POST["nombre"]; // Asignar el valor del campo "nombre" del formulario a la variable $nombre
        $apellido = $_POST["apellido"]; // Asignar el valor del campo "apellido" del formulario a la variable $apellido
    }
?>

<!DOCTYPE html>
<html>
<head>
    <title>Confirmación</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    <h1>Gracias por enviar el formulario<br></h1>
    <p>Aquí están los datos que hemos recibido:<br></p>
    <ul>
        <li><strong>Nombre:</strong> <?php echo $nombre; ?><br></li>
        <br><li><strong>Apellido:</strong> <?php echo $apellido; ?></li>
        <!-- Se utilizan para imprimir los valores de las variables $nombre y $apellido -->

    </ul>
    <a href="../index.php"><button type="button" class="btn btn-dark">Volver al inicio</button></a>
</body>
</html>

<?php

require_once("../modelo/gestion_datos.php"); // Incluir el archivo gestion_datos.php

?>