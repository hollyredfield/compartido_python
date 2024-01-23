<?php


//Apertura de ficheros de texto

$archivo = fopen("prueba.txt", "a");

//Los modos de apertura de los ficheros son

//w: Abre el archivo para escritura desde el principio.
//a: Abre el archivo para escritura desde la última línea que contenga. 
//r: Abre el archivo para lectura.

//Cierre de archivos de texto

//fclose($archivo);

//Escritura de archivos de texto.

fwrite($archivo, "Linea añadida desde código al archivo de texto." . PHP_EOL);
fwrite($archivo, "Esta es otra línea añadida desde código y es la segunda porque va desupes de la primera" . PHP_EOL);
fclose($archivo);

//Lectura de archivos de texto
$archivo = fopen("prueba.txt", "r");

while (!feof($archivo)) {
    $linea = fgets($archivo);
    echo $linea;
}

fclose($archivo);

//Mejora de la lectura mediante comprobación de existencia de fichero

$nombre_archivo = "pruebo.txt";

echo PHP_EOL."*************** Segunda lectura con comprobación ********".PHP_EOL;

if (file_exists($nombre_archivo)) {
    $archivo = fopen($nombre_archivo, "r");

    while (!feof($archivo)) {
        $linea = fgets($archivo);
        echo $linea;
    }

    fclose($archivo);
}else{
    echo "El archivo que estas intentando leer no existe";
}
