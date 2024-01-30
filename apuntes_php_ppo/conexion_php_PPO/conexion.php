<?php // Inicio del bloque de código PHP

class ConexionBD { // Definición de la clase ConexionBD

    private $host = "localhost"; // Propiedad que almacena el host de la base de datos
    private $usuario = "root"; // Propiedad que almacena el nombre de usuario de la base de datos
    private $contrasena = ""; // Propiedad que almacena la contraseña de la base de datos
    private $nombreBD = "SoloCrossFit"; // Propiedad que almacena el nombre de la base de datos
    private $conexion; // Propiedad que almacena la conexión a la base de datos

    public function abrirConexion() { // Método para abrir la conexión a la base de datos
        $this->conexion = new mysqli($this->host, $this->usuario, $this->contrasena, $this->nombreBD); // Creación de la conexión

        if ($this->conexion->connect_error) { // Si hay un error en la conexión
            die("Error de conexión: " . $this->conexion->connect_error); // Muestra el error y termina la ejecución del script
        } else { // Si no hay error en la conexión
            echo "Conexión exitosa"; // Muestra un mensaje de éxito
        }
    }
    public function getConexion() { // Método para obtener la conexión
        return $this->conexion; // Devuelve la conexión
    }

    public function cerrarConexion() { // Método para cerrar la conexión a la base de datos
        if ($this->conexion) { // Si la conexión existe
            $this->conexion->close(); // Cierra la conexión
            $this->conexion = null; // Establece la propiedad de conexión en null
            echo "La conexión se ha cerrado con éxito, pillín ;)"; // Muestra un mensaje de éxito
        } else { // Si la conexión no existe
            echo "La conexión ya estaba cerrada."; // Muestra un mensaje indicando que la conexión ya estaba cerrada
        }
    }
} // Fin de la definición de la clase ConexionBD


?> // Fin del bloque de código PHP
