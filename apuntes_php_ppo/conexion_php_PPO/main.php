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





//$stmt->bind_param("ssdsiisds", $nombre, $plan_trabajo, $peso_actual, $categoria_peso, $eventos_mes, $horas_extras_mes, $gastos_detallados, $costo_total, $comparacion_peso_categoria);

// El método bind_param se utiliza para vincular variables a los marcadores de posición en una sentencia SQL preparada.

// El primer argumento de bind_param es una cadena que especifica el tipo de cada uno de los marcadores de posición en la sentencia SQL. En tu caso, "ssdsiisds" significa:

// "s": string
// "d": double
// "i": integer
// Por lo tanto, "ssdsiisds" indica que los marcadores de posición en tu sentencia SQL son, en orden: string, string, double, string, integer, integer, string, double, string.

// Los argumentos siguientes a la cadena de tipos son las variables que quieres vincular a los marcadores de posición. Estas variables deben ser pasadas por referencia, no por valor. En tu caso, estás vinculando las variables $nombre, $plan_trabajo, $peso_actual, etc., a los marcadores de posición en tu sentencia SQL.

// Por lo tanto, la línea de código que mencionaste está vinculando las variables a los marcadores de posición en la sentencia SQL preparada, y especificando el tipo de cada marcador de posición.

// El uso de bind_param en las consultas preparadas en PHP no es obligatorio, pero es altamente recomendado por varias razones:

// Seguridad: Las consultas preparadas con bind_param ayudan a prevenir los ataques de inyección SQL, ya que los valores de las variables se envían al servidor de la base de datos de manera separada y no se permiten interferir con la consulta en sí.

//Eficiencia: Si estás ejecutando la misma consulta muchas veces con diferentes valores, las consultas preparadas pueden ser más eficientes. El servidor de la base de datos puede optimizar la ejecución de la consulta al prepararla una vez y luego ejecutarla con diferentes valores.

// Conveniencia: bind_param maneja automáticamente la escapada de caracteres especiales en las cadenas, lo que puede ser un proceso tedioso y propenso a errores si se hace manualmente.

// Para operaciones de borrado o modificación, el uso de bind_param sería similar. Por ejemplo, para una operación de borrado podrías tener algo como esto:

    // $stmt = $conexion->getConexion()->prepare("DELETE FROM usuarios WHERE id = ?");
    // $stmt->bind_param("i", $id);

// Y para una operación de modificación podrías tener algo como esto:

    // $stmt = $conexion->getConexion()->prepare("UPDATE usuarios SET nombre = ? WHERE id = ?");
    // $stmt->bind_param("si", $nombre, $id);

