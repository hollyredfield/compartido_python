from bdd import ConexionBiblioteca
from mysqlx import Error
from crud_lector import *

class Libro:

    def __init__(self, autor, titulo, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        
        self.conexion = ConexionBiblioteca()
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.paginas = paginas
        self.año_publicacion = anio_publicacion
        self.edicion = edicion
        self.idioma = idioma
        self.ISBN = ISBN
        self.prestamos_realizados = prestamos_realizados
        self.prestado = prestado

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False

    def devolver(self):
        self.prestado = False 

    def set_autor(self, autor):
        self.autor = autor
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def get_titulo(self):
        return self.titulo
    
    def set_genero(self, genero):
        self.genero = genero
    
    def get_genero(self):
        return self.genero
    
    def set_paginas(self, paginas):
        self.paginas = paginas
    
    def get_paginas(self):
        return self.paginas

    def set_año_publicacion(self, año_publicacion):
        self.año_publicacion = año_publicacion
    
    def get_año_publicacion(self):
        return self.año_publicacion
    
    def set_edicion(self, edicion):
        self.edicion = edicion
    
    def get_edicion(self):
        return self.edicion
    
    def set_idioma(self, idioma):
        self.idioma = idioma
    
    def get_idioma(self):
        return self.idioma
    
    def set_ISBN(self, ISBN):
        self.ISBN = ISBN
    
    def get_ISBN(self):
        return self.ISBN

    def set_prestamos_realizados(self, prestamos_realizados):
        self.idioma = prestamos_realizados
    
    def get_prestamos_realizados(self):
        return self.prestamos_realizados
    
    def set_prestado(self, prestado):
        self.prestado = prestado
    
    def get_prestado(self):
        return self.prestado
    
    def alta_libro(self, autor, titulo, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        try:
            conexion = self.conexion.conectar()
            cursor = conexion.cursor()

            query = "INSERT INTO libros (autor, titulo, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (autor, titulo, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado)

            cursor.execute(query, valores)
            conexion.commit()
            print('Alta de libro realizada con éxito')
            self.conexion.cierra_conexion(conexion)
        except Error as error:
            print(f"Error en alta de libro: {error}")
            return None
    
    def borrar_libro(self, id_libro):
        try:

            if self.esta_prestado(id_libro):
                print("No se puede borrar el libro porque está prestado.")
                return None

            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = "DELETE FROM libros WHERE id_libro = %s"
            valores = (id_libro,)
            cursor.execute(query, valores)
            conexion.commit()
            print("libro eliminado con éxito.")
            self.conexion.cierra_conexion(conexion)
            
        except Error as error:
            print(f"Error en borrar libro: {error}")   
            return None
        
    def esta_prestado(self, id_libro):
        try:
            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = "SELECT COUNT(*) FROM prestamos WHERE libro = %s AND fecha_devolucion IS NULL"
            valores = (id_libro,)
            cursor.execute(query, valores)
            interruptor = cursor.fetchone()[0]
            self.conexion.cierra_conexion(conexion)
            return interruptor > 0
            
        except Error as error:
            print(f"Error en verificar si el libro está prestado: {error}")
            return True 