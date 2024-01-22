<?php
$nombre = $_POST['nombre'];
$apellidos = $_POST['apellidos'];
echo "Confirmación: " . $nombre . " " . $apellidos;
?>
<?php
require_once '/modelo/gestion_datos.php';

echo "Confirmación" .$nombre . " " . $apellidos . ". " . $mensaje;


?>