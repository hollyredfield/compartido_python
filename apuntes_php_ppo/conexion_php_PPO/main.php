<?php
// crud de solo insertar datos
require_once('conexion.php');

function insertarUsuario() {
    // Crear una nueva instancia de la clase ConexionBD
    $conexion = new ConexionBD();
    // Abrir la conexión
    $conexion->abrirConexion();

    // Solicita al usuario que introduzca los datos
    $nombre = readline("Introduce el nombre: ");
    $plan_trabajo = readline("Introduce el plan de trabajo: ");
    $peso_actual = readline("Introduce el peso actual: ");
    $categoria_peso = readline("Introduce la categoría de peso: ");
    $eventos_mes = readline("Introduce el número de eventos este mes: ");
    $horas_extras_mes = readline("Introduce el número de horas extras este mes: ");
    $gastos_detallados = readline("Introduce los gastos detallados: ");
    $costo_total = readline("Introduce el costo total: ");
    $comparacion_peso_categoria = readline("Introduce la comparación de peso y categoría: ");

    // Prepara la consulta SQL
    $stmt = $conexion->getConexion()->prepare("INSERT INTO usuarios (nombre, plan_trabajo, peso_actual, categoria_peso, eventos_mes, horas_extra_mes, gastos_detallados, costo_total, comparacion_peso_categoria) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)");

    if ($stmt === false) {
        die("Error preparando la consulta: " . $conexion->getConexion()->error);
    }
    

    
    // Vincula los parámetros a la consulta SQL
    $stmt->bind_param("ssdsiisds", $nombre, $plan_trabajo, $peso_actual, $categoria_peso, $eventos_mes, $horas_extras_mes, $gastos_detallados, $costo_total, $comparacion_peso_categoria);

    // Ejecuta la consulta
    $stmt->execute();

    // Comprueba si la inserción fue exitosa
    if ($stmt->affected_rows > 0) {
        echo "Usuario insertado con éxito.";
    } else {
        echo "Error al insertar el usuario.";
    }

    // Cierra la consulta
    $stmt->close();

    // Cerrar la conexión
    $conexion->cerrarConexion();
}

// Llamar a la función
insertarUsuario();
?>
