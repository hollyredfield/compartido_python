<?php

$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];

$datos = $nombre . '; ' . $apellido . PHP_EOL;

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