from conexion import Conexion
import mysql.connector
class Libro:
    def __init__(self, titulo=None, autor=None, genero=None, paginas=None, anio_publicacion=None, edicion=None, idioma=None, ISBN=None, prestamos_realizados=None, prestado=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.edicion = edicion
        self.idioma = idioma
        self.ISBN = ISBN
        self.prestamos_realizados = prestamos_realizados
        self.prestado = prestado

    def dar_alta(self):
        try:
            titulo = input("Introduce el título: ")
            autor = input("Introduce el autor: ")
            genero = input("Introduce el género: ")
            paginas = int(input("Introduce el número de páginas: "))
            anio_publicacion = int(input("Introduce el año de publicación: "))
            edicion = int(input("Introduce la edición: "))
            idioma = input("Introduce el idioma: ")
            ISBN = input("Introduce el ISBN: ")
            prestamos_realizados = int(input("Introduce el número de préstamos realizados: "))
            prestado = bool(input("¿Está prestado? (True/False): "))

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "INSERT INTO libros (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha dado de alta con éxito el libro")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al añadir el libro. ", error)
            return None
    def ver_libros(self):
        try:
            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "select * from libros"
            cursor.execute(query)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al ver los libros. ", error)
            return None
    def modificar(self, id_libro):
        try:
            titulo = input("Introduce el nuevo título: ")
            autor = input("Introduce el nuevo autor: ")
            genero = input("Introduce el nuevo género: ")
            paginas = int(input("Introduce el nuevo número de páginas: "))
            anio_publicacion = int(input("Introduce el nuevo año de publicación: "))
            edicion = int(input("Introduce la nueva edición: "))
            idioma = input("Introduce el nuevo idioma: ")
            ISBN = input("Introduce el nuevo ISBN: ")
            prestamos_realizados = int(input("Introduce el nuevo número de préstamos realizados: "))
            prestado = bool(input("¿Está prestado? (True/False): "))

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "UPDATE libros SET titulo = %s, autor = %s, genero = %s, paginas = %s, anio_publicacion = %s, edicion = %s, idioma = %s, ISBN = %s, prestamos_realizados = %s, prestado = %s WHERE id_libro = %s"
            valores = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado, id_libro)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha modificado con éxito el libro")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al modificar el libro. ", error)
            return None
    def buscar_libro(self):
        try:
            id_libro = int(input("Introduce el id del libro: "))
            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "SELECT * FROM libros WHERE id_libro = %s"
            valores = (id_libro,)
            cursor.execute(query, valores)
            libro = cursor.fetchone()  # Leer los resultados antes de hacer commit
            if libro is not None:
                print("Se ha encontrado con éxito el libro:", libro)
            else:
                print("No se encontró ningún libro con el ID proporcionado.")
            conexion.conexion.commit()
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al buscar el libro. ", error)
            return None
    def eliminar_libro(self):
        try:
            id_libro = input("Introduce el ID del libro a eliminar: ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "DELETE FROM libros WHERE id_libro = %s"
            valores = (id_libro,)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha eliminado con éxito el libro")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al eliminar el libro. ", error)
            return None



""" 
class Menu:
    def __init__(self):
        self.libro = Libro()

    def mostrar_menu(self):
        print("\n1. Dar de alta un libro")
        print("2. Ver todos los libros")
        print("3. Modificar un libro")
        print("4. Buscar un libro")
        print("5. Eliminar un libro")
        print("6. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.libro.dar_alta()
        elif opcion == 2:
            self.libro.ver_libros()
        elif opcion == 3:
            id_libro = int(input("Introduce el ID del libro a modificar: "))
            self.libro.modificar(id_libro)
        elif opcion == 4:
            self.libro.buscar_libro()
        elif opcion == 5:
            self.libro.eliminar_libro()
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

def main():
    menu = Menu()
    while True:
        menu.mostrar_menu()
        opcion = int(input("Elige una opción: "))
        menu.ejecutar_opcion(opcion)
        if opcion == 6:
            break

if __name__ == "__main__":
    main()
"""