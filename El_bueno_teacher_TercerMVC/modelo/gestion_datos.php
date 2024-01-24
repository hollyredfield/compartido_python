<?php
function guardardatos($nombre, $apellidos){
    $archivo = fopen("../modelo/datos.dat", "a");
    fwrite($archivo, "$nombre; $apellidos" . PHP_EOL);
    fclose($archivo);
}

function mostrar(){  
    $archivo = fopen("../modelo/datos.dat", "r");
    $resultados = array();  // Almacenar resultados en un array

    while (!feof($archivo)) {
        $linea = fgets($archivo);
        $resultados[] = $linea;
    }
    fclose($archivo);
    return $resultados;  // Devolver array con todas las líneas
}
?>
