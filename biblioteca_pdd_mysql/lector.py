import mysql.connector
from conexion import Conectar   
class Lectores:
    def __init__(self, id_alta, nombre, apellidos, fecha_alta, fecha_baja):
        self.id_alta = id_alta
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
    def verlectores(self):
        print("ID: ", self.id_alta)
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)
        print("Fecha de alta: ", self.fecha_alta)
        print("Fecha de baja: ", self.fecha_baja)
    def buscarlectores(self, nombre, apellidos):
        if self.nombre == nombre or self.apellidos == apellidos:
            return True
        return False
    def eliminarlectores(self, nombre, id_alta):
        if self.nombre == nombre or self.id_alta == id_alta:
            return True
        return False
    
    
