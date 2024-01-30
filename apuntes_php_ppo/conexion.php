<?php

class ConexionBiblioteca {

    private $conexion;

    public function conectar() {
        $this->conexion = new mysqli('localhost', 'root', 'DAM1', 'biblioteca');

        if ($this->conexion->connect_error) {
            die("Error en conexión: " . $this->conexion->connect_error);
        }

        echo "Conexión exitosa.";
    }

    public function cierra_conexion() {
        if ($this->conexion) {
            $this->conexion->close();
            echo "Conexión cerrada.";
        }
    }
}