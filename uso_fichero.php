<?php
$archivo = fopen("Prueba.txt", "a"); // se puede usar append (a) o (w) para sobreecribir, solo se puede eliminar el archivo si está
//en modo (W)
//

fwrite($archivo, "Línea añadida desde código " .PHP_EOL);
fwrite($archivo, "Esta es otra otra línea más añadida " . PHP_EOL);
fclose($archivo);
//fwrite($archivo,"HAAHAHAHAHAH". PHP_EOL); //no puede porque el archivo ya ha sido cerrado.
//este programa lee todas las líneas de un fichero y las lee línea por línea mientras se cumpla la condición de que siga mientras no llegue al final    del fichero con feof
$archivo = fopen("prueba.txt", "r");
while(!feof($archivo)) { //feof, bucle, mientras no llegues al final del archivo, continúa. 
    $linea = fgets($archivo); //fget es leer línea y es como un realines en python, y trim es para quitar los espacios. 
    echo $linea;
}
?>



