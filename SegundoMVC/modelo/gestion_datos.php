<?php
$nombre = $_POST['nombre'];
$apellidos = $_POST['apellidos'];
$datos = $nombre . '; ' . $apellidos . PHP_EOL; 
$archivo = 'datos.dat';

$file = fopen($archivo, 'a');
if (fwrite($file, $datos)) {
    echo 'enhorabuena';

} else {
    echo ' HAHAHAHAHA';
}
fclose ($file);




if (file_exists($archivo)) {
    echo "Los datos se han grabado correctamente";
} else {
    echo "Ha habido problemas para poder grabar los archivos";
}

?>