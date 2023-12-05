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
    
    
class LectoresCRUD:
    def __init__(self, db):
        self.db = db

    def create_lector(self, lector):
        try:
            conexion = self.db.conexion_bdd()
            cursor = conexion.cursor()
            query = "INSERT INTO lectores (id_alta, nombre, apellidos, fecha_alta, fecha_baja) VALUES (%s, %s, %s, %s, %s)"
            values = (lector.id_alta, lector.nombre, lector.apellidos, lector.fecha_alta, lector.fecha_baja)
            cursor.execute(query, values)
            conexion.commit()
            self.db.cerrar_conexion(conexion)
        except mysql.connector.Error as e:
            print("Error al crear lector: ", e)

    def read_lector(self, id_alta):
        try:
            conexion = self.db.conexion_bdd()
            cursor = conexion.cursor()
            query = "SELECT * FROM lectores WHERE id_alta = %s"
            cursor.execute(query, (id_alta,))
            lector = cursor.fetchone()
            self.db.cerrar_conexion(conexion)
            return lector
        except mysql.connector.Error as e:
            print("Error al leer lector: ", e)  

conectar = Conectar()
crud = LectoresCRUD(conectar)
lector = Lectores(id_alta=1, nombre='John', apellidos='Doe', fecha_alta='2022-01-01', fecha_baja='2022-12-31')
crud.create_lector(lector)
conexion = self.db.conexion_bdd()