from bdd import ConexionBiblioteca
from mysqlx import Error

class Prestamos:

    def __init__(self, fecha_prestamo, libro, lector, fecha_devolucion):
        
        self.conexion = ConexionBiblioteca()
        self.fecha_prestamo = fecha_prestamo
        self.libro = libro
        self.fecha_devolucion = fecha_devolucion
        self.lector = lector
    
    def get_fecha_prestamo(self):
        return self.fecha_prestamo
    
    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def get_libro(self):
        return self.libro
    
    def set_libro(self, libro):
        self.libro = libro

    def get_autor(self):
        return self.lector
    
    def set_titulo(self, lector):
        self.lector = lector
        
    def get_devolucion(self):
        return self.fecha_devolucion
    
    def set_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion

    def realizar_prestamo(self, id_prestamo, fecha_prestamo, libro, lector):
        try:

            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = "INSERT INTO prestamos (id_prestamo, fecha_prestamo, libro, lector) VALUES (%s, %s, %s, %s)"
            valores = [id_prestamo, fecha_prestamo, libro, lector]
            cursor.execute(query, valores)
            conexion.commit()
            print('Prestamo realizado con éxito')
            self.conexion.cierra_conexion(conexion)
        except Error as error:
            print(f"Error en crear prestamo: {error}")
            return None
 
    def realizar_devolucion(self, id_prestamo, fecha_prestamo, libro, lector,fecha_devolucion):
        try:

            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = "UPDATE prestamos SET fecha_devolucion = %s WHERE id_prestamo = %s"
            valores = [fecha_devolucion, id_prestamo]
            cursor.execute(query, valores)
            conexion.commit()
            print('Devolución del prestamo realizado con éxito')
            self.conexion.cierra_conexion(conexion)
        except Error as error:
            print(f"Error en crear devolución: {error}")
            return None
        
    def ver_libro_prestado(self, fecha_prestamo, libro, lector):
        try:
            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = """
                SELECT libros.titulo AS nombre_libro, lectores.nombre AS nombre_lector, lectores.apellidos AS apellidos_lector, prestamos.fecha_prestamo
                FROM prestamos
                JOIN libros ON prestamos.libro = libros.id_libro
                JOIN lectores ON prestamos.lector = lectores.id_lector
                WHERE prestamos.fecha_prestamo = %s AND prestamos.libro = %s AND prestamos.lector = %s
            """
            cursor.execute(query, (fecha_prestamo, libro, lector))

            for (nombre_libro, nombre_lector, apellidos_lector, fecha_prestamo) in cursor:
                print(f"Fecha del préstamo: {fecha_prestamo} Libro prestado: {nombre_libro} Prestado a: {nombre_lector} {apellidos_lector}")

            conexion.commit()
            self.conexion.cierra_conexion(conexion)
        except Error as error:
            print(f"Error en seleccionar préstamo: {error}")
            return None


