<!DOCTYPE html>
<html>
<head>
    <title>Tabla Datos</title>
</head>
<body>
    <?php
    $archivo = '../datos.dat';
    $file = fopen($archivo, 'r');
    echo "<table>";
    while (($line = fgets($file)) !== false) {
        $datos = explode('; ', $line);
        echo "<tr><td>".$datos[0]."</td><td>".$datos[1]."</td></tr>";
    }
    echo "</table>";
    fclose($file);
    ?>
    <a href="../index.php">Volver al menú principal</a>
</body>
</html>