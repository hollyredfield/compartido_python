-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-11-2023 a las 12:29:48
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: SoloCrossfit
--
CREATE DATABASE IF NOT EXISTS SoloCrossfit;
USE SoloCrossfit;

--
-- Estructura de tabla para la tabla usuarios
--

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    plan_trabajo VARCHAR(50) NOT NULL,
    peso_actual DECIMAL(5,2) NOT NULL,
    categoria_peso VARCHAR(20) NOT NULL,
    eventos_mes INT NOT NULL,
    horas_extra_mes INT NOT NULL,
    gastos_detallados TEXT,
    costo_total DECIMAL(8,2) NOT NULL,
    comparacion_peso_categoria VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Estructura de tabla para la tabla eventos_competiciones
--

CREATE TABLE eventos_competiciones (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    numero_eventos_mes INT,
    horas_entrenamiento_semana INT,
    fecha_evento DATE,
    costo_total DECIMAL(8,2)
    -- Otros campos según sea necesario
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla usuarios
--
ALTER TABLE usuarios
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla eventos_competiciones
--
ALTER TABLE eventos_competiciones
  MODIFY id_evento int(11) NOT NULL AUTO_INCREMENT;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;