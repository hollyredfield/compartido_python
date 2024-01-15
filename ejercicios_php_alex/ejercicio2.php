Ejercicio 2: Encontrar el Mayor y el Menor

Crea un programa que solicite al usuario introducir una serie de números enteros (terminando cuando el usuario ingrese un valor negativo). Una vez finalizada la introducción de datos, debe mostrar y encontrar el número más grande y el más pequeño de los números introducidos.
<?php
$numeros = array();

while (true) {
    $input = readline("Introduce un número entero (introduce un número negativo para terminar): ");
    $numero = intval($input);

    if ($numero < 0) {
        break;
    }

    array_push($numeros, $number);
}

if (count($numeros) > 0) {
    echo "El número más grande es: " . max($numeros) . "\n";
    echo "El número más pequeño es: " . min($numeros) . "\n";
} else {
    echo "No se introdujo ningún número.\n";
}
?>


//$lista_numeros = array();
//$intenumeros = readline("Introduce una serie de números separados por comas o espacios: ");

// Divide la entrada del usuario en un array
//$intenumeros_array = preg_split('/[ ,]+/', $intenumeros);

// Recorre el array y añade cada número a $lista_numeros
//foreach ($intenumeros_array as $numero) {
    //array_push($lista_numeros, intval($numero));
//}

//print_r($lista_numeros); // Imprime el array para verificar

