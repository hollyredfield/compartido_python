
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
    
    
"""
id_lector int NOT NULL AUTO_INCREMENT
nombre VARCHAR
apellidos VARCHAR
fecha_alta DATE
fecha_baja DATE 
"""
from conexion import Conectar
from libro import Libro
class Lector:
    def __init__(self, db):
        self.db = db
    def add_lector(self, nombre, apellidos, fecha_alta, fecha_baja):
        cursor = self.db.conexion.cursor()
        add_lector_query = ("INSERT INTO lectores "
                          "(nombre, apellidos, fecha_alta, fecha_baja) "
                          "VALUES (%s, %s, %s, %s)")
        lector_data = (nombre, apellidos, fecha_alta, fecha_baja)
        cursor.execute(add_lector_query, lector_data)
        self.db.conexion.commit()
        cursor.close()
        print("Lector agregado correctamente.")
    def ver_lectores(self):
        cursor = self.db.conexion.cursor()
        ver_lectores_query = ("SELECT * FROM lectores")
        cursor.execute(ver_lectores_query)
        lectores = cursor.fetchall()
        cursor.close()
        print(lectores)
        return lectores
        
    def buscar_lector(self, nombre):
        cursor = self.db.conexion.cursor()
        buscar_lector_query = ("SELECT * FROM lectores WHERE nombre = %s")
        cursor.execute(buscar_lector_query, (nombre,))
        lector = cursor.fetchone()
        cursor.close()
        print(lector)
        return lector
    def eliminar_lector(self, nombre):
        cursor = self.db.conexion.cursor()
        eliminar_lector_query = ("DELETE FROM lectores WHERE nombre = %s")
        cursor.execute(eliminar_lector_query, (nombre,))
        self.db.conexion.commit()
        cursor.close()
        print("Lector eliminado corretamente.")
    def modificar_lector(self, nombre, apellidos, fecha_alta, fecha_baja):
        cursor = self.db.conexion.cursor()
        modificar_lector_query = ("UPDATE lectores SET nombre = %s, apellidos = %s, fecha_alta = %s, fecha_baja = %s WHERE nombre = %s")
        lector_data = (nombre, apellidos, fecha_alta, fecha_baja, nombre)
        cursor.execute(modificar_lector_query, lector_data)
        self.db.conexion.commit()
        cursor.close()
        print("Lector modificado correctamente.")
conexion = Conectar()
conexion.conexion_bdd()
lector = Lector(conexion)
lector.modificar_lector("Marcos", "Perez", "2020-01-01", "2020-01-01")
conexion.close_connection()