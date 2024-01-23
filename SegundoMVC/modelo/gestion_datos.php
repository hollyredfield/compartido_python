<?php
$nombre = $_POST['nombre'];
$apellidos = $_POST['apellidos'];
$datos = $nombre . '; ' . $apellidos . PHP_EOL;
$archivo = '../datos.dat';
$file = fopen($archivo, 'a');
if (fwrite($file, $datos)) {
    $mensaje = 'Los datos se han grabado correctamente';
} else {
    $mensaje = 'Ha habido problemas para poder grabar los archivos';
}
fclose ($file);
return $mensaje;
?>
