from conexion import Conectar
class Libro:
    def __init__(self, db):
        self.db = db

    def add_book(self, titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        cursor = self.db.conexion.cursor()
        add_book_query = ("INSERT INTO libros "
                          "(titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) "
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        book_data = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado)
        cursor.execute(add_book_query, book_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro agregado correctamente.")

    def ver_libros(self):
        cursor = self.db.conexion.cursor()
        ver_libros_query = ("SELECT * FROM libros")
        cursor.execute(ver_libros_query)
        libros = cursor.fetchall()
        cursor.close()
        return libros

    def buscar_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        buscar_libro_query = ("SELECT * FROM libros WHERE titulo = %s")
        cursor.execute(buscar_libro_query, (titulo,))
        libro = cursor.fetchone()
        cursor.close()
        print(libro)
        return libro
    def eliminar_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        eliminar_libro_query = ("DELETE FROM libros WHERE titulo = %s")
        cursor.execute(eliminar_libro_query, (titulo,))
        self.db.conexion.commit()
        cursor.close()
        print("Libro eliminado corretamente.")

    def modificar_libro(self, titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        cursor = self.db.conexion.cursor()
        modificar_libro_query = ("UPDATE libros SET titulo = %s, autor = %s, genero = %s, paginas = %s, anio_publicacion = %s, edicion = %s, idioma = %s, ISBN = %s, prestamos_realizados = %s, prestado = %s WHERE titulo = %s")
        libro_data = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado, titulo)
        cursor.execute(modificar_libro_query, libro_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro modificado correctamente.")
    def prestra_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        prestar_libro_query = ("UPDATE libros SET prestado = %s WHERE titulo = %s")
        libro_data = (True, titulo)
        cursor.execute(prestar_libro_query, libro_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro prestado correctamente.")
    def devolver_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        devolver_libro_query = ("UPDATE libros SET prestado = %s WHERE titulo = %s")
        libro_data = (False, titulo)
        cursor.execute(devolver_libro_query, libro_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro devuelto correctamente.")