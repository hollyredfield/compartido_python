
¿<?php
require_once('conexion.php');

$xd = new ConexionBD;
$xd-> cerrarConexion();
$xd->abrirConexion();
?>