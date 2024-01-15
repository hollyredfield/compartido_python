Ejercicio 3: Tabla de multiplicar.

Crea un programa que solicite al usuario un número y muestre la tabla de multiplicar de ese número del 1 al 10. Utiliza un bucle para generar las multiplicaciones. 

<?php

$input = readline("Dame un número entero: ") ;
$numero = intval($input);
echo "Has introduido el número $numero . \n";
for ($number = 1; $number <= 10; $number++) {
    echo $number . " x " . $numero * $number . "\n" ;
}
?>
//
//$input = readline("Dame un número entero: ");
//$numero = intval($input);
//echo "Has introducido el número: " . $numero . "\n";

//for ($i = 1; $i <= 10; $i++) {
    //echo $numero . " x " . $i . " = " . $numero * $i . "\n";
//}
//