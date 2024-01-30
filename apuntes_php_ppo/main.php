<?php

require_once('class_coche.php');
require_once('class_coche2.php');

$coche = new Coche('Rojo', 'Toyota RAV4');

echo 'El color del coche es: '.$coche->get_color().PHP_EOL;
echo 'El modelo del coche es: '.$coche->get_modelo().PHP_EOL;
echo '**********************************************************'.PHP_EOL;
$coche2 = new Coche2();

echo 'El color del coche2 es: '.$coche2->get_color().PHP_EOL;
echo 'El modelo del coche2 es: '.$coche2->get_modelo().PHP_EOL;

echo '**********************************************************'.PHP_EOL;

$coche2->set_color('Gris');
$coche2->set_modelo('BMW X3');

echo '**********************************************************'.PHP_EOL;

echo 'El color del coche2 es: '.$coche2->get_color().PHP_EOL;
echo 'El modelo del coche2 es: '.$coche2->get_modelo().PHP_EOL;

echo '**********************************************************'.PHP_EOL;

$coche2->ver_atributos();

$coche3 = new Coche2();

$coche4 = new Coche('Azul', 'Mercedes GLC');

echo "El color de coche4 es ".$coche4->get_color().PHP_EOL;

echo "El color de coche3 es ".$coche3->get_color().PHP_EOL;

$coche3->set_color("Blanco");

echo "El color de coche3 es ".$coche3->get_color().PHP_EOL;

echo "El color de coche es: ".$coche->get_color().PHP_EOL;

echo "Cambiamos el color del objeto coche".PHP_EOL;
$coche->set_color("Azul Oscuro").PHP_EOL;

echo "El color de coche es: ".$coche->get_color().PHP_EOL;

?>