class Prestamos_local:
    def __init__(self, fecha_prestamo, libro, lector, fecha_devolucion):
        self.fecha_prestamo = fecha_prestamo
        self.libro = libro
        self.lector = lector
        self.fecha_devolucion = fecha_devolucion
    def ver_prestamos(self):
        print("Fecha de prestamo: ", self.fecha_prestamo)
        print("Libro: ", self.libro)
        print("Lector: ", self.lector)
        print("Fecha de devolución: ", self.fecha_devolucion)
    def buscar_prestamos(self, libro, lector):
        if self.libro == libro or self.lector == lector:
            return True
        return False
    def dar_de_baja(self, libro, lector):
        if self.libro == libro or self.lector == lector:
            return True
        return False
    def modificar_prestamos(self, libro, lector):
        if self.libro == libro or self.lector == lector:
            return True
        return False
""" 
id_prestamo INT NOT NULL AUTO_INCREMENT
fecha_prestamo DATE
libro INT
lector INT
feha_devolucion DATE 
"""

from conexion import Conectar
from libro import Libro
from lector import Lector
class Prestamo:
    def __init__(self, db):
        self.db = db
    def add_prestamo(self, fecha_prestamo, libro, lector, fecha_devolucion):
        cursor = self.db.conexion.cursor()
        add_prestamo_query = ("INSERT INTO prestamos "
                           "(fecha_prestamo, libro, lector, fecha_devolucion) "
                           "VALUES (%s, %s, %s, %s)")
        prestamo_data = (fecha_prestamo, libro, lector, fecha_devolucion)
        cursor.execute(add_prestamo_query, prestamo_data)
        self.db.conexion.commit()
        cursor.close()
        print("Prestamo agregado correctamente.")
    def ver_prestamos(self):
        cursor = self.db.conexion.cursor()
        ver_prestamos_query = ("SELECT * FROM prestamos")
        cursor.execute(ver_prestamos_query)
        prestamos = cursor.fetchall()
        cursor.close()
        print(prestamos)
        return prestamos
    def buscar_prestamo(self, libro):
        cursor = self.db.conexion.cursor()
        buscar_prestamo_query = ("SELECT * FROM prestamos WHERE libro = %s")
        cursor.execute(buscar_prestamo_query, (libro,))
        prestamo = cursor.fetchone()
        cursor.close()
        print(prestamo)
        return prestamo
    def eliminar_prestamo(self, libro):
        cursor = self.db.conexion.cursor()
        eliminar_prestamo_query = ("DELETE FROM prestamos WHERE libro = %s")
        cursor.execute(eliminar_prestamo_query, (libro,))
        self.db.conexion.commit()
        cursor.close()
        print("Prestamo eliminado corretamente.")
    def modificar_prestamo(self, libro, lector):
        cursor = self.db.conexion.cursor()
        modificar_prestamo_query = ("UPDATE prestamos SET libro = %s, lector = %s WHERE libro = %s")
        prestamo_data = (libro, lector, libro)
        cursor.execute(modificar_prestamo_query, prestamo_data)
        self.db.conexion.commit()
        cursor.close()
        print("Prestamo modificado correctamente.")

conect = Conectar()
conect.conexion_bdd()
prestamo = Prestamo(conect)
prestamo.ver_prestamos()
conect.close_connection()