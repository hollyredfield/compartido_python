<?php
require_once ('../modelo/gestion_datos.php');

/*
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];
    $apellidos = $_POST["apellidos"];
}else{
    header("Location: /TercerMVC/index.php");
}
*/
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];
    $apellidos = $_POST["apellidos"];
}


if (isset($_POST['accion'])){
    $accion = $_POST['accion'];
}else{
    $accion = "";
}

switch($accion){
    case "grabar":
        guardardatos($nombre,$apellidos);
        break;
    case "":
        include ("../vistas/tabladatos.php");
        break;
}
?>
