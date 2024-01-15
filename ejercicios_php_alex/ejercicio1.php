Ejercicio 1: Suma de números pares

Crea un programa que genera un array de números enteros del 1 al 20 y luego use un bucle para calcular la suma de todos los números pares en el array

<?php
$numeros = range(1,20);

$suma = 0;
foreach ($numeros as $numero) {
    if ($numero %2 == 0) {
        
        $suma+=$numero;
    } 

}

echo "La suma de los números pares es $suma " ;
?>