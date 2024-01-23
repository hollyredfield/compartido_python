from conexion import Conexion
import mysql.connector
class Prestamo:
    def __init__(self, id_prestamo=None, fecha_prestamo=None, libro=None, lector=None, fecha_devolucion=None):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.libro = libro
        self.lector = lector
        self.fecha_devolucion = fecha_devolucion

    def dar_alta(self):
        try:
            fecha_prestamo = input("Introduce la fecha de préstamo: ")
            libro = int(input("Introduce el ID del libro: "))
            lector = int(input("Introduce el ID del lector: "))
            fecha_devolucion = input("Introduce la fecha de devolución: ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "INSERT INTO prestamos (fecha_prestamo, libro, lector, fecha_devolucion) VALUES (%s, %s, %s, %s)"
            valores = (fecha_prestamo, libro, lector, fecha_devolucion)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha dado de alta con éxito el préstamo")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al añadir el préstamo. ", error)
            return None

    def ver_prestamos(self):
        try:
            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "select * from prestamos"
            cursor.execute(query)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al ver los préstamos. ", error)
            return None

    def modificar(self, id_prestamo):
        try:
            fecha_prestamo = input("Introduce la nueva fecha de préstamo: ")
            libro = int(input("Introduce el nuevo ID del libro: "))
            lector = int(input("Introduce el nuevo ID del lector: "))
            fecha_devolucion = input("Introduce la nueva fecha de devolución: ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "UPDATE prestamos SET fecha_prestamo = %s, libro = %s, lector = %s, fecha_devolucion = %s WHERE id_prestamo = %s"
            valores = (fecha_prestamo, libro, lector, fecha_devolucion, id_prestamo)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha modificado con éxito el préstamo")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al modificar el préstamo. ", error)
            return None

    def buscar_prestamo(self):
        try:
            id_prestamo = int(input("Introduce el id del préstamo: "))
            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "SELECT * FROM prestamos WHERE id_prestamo = %s"
            valores = (id_prestamo,)
            cursor.execute(query, valores)
            prestamo = cursor.fetchone()
            if prestamo is not None:
                print("Se ha encontrado con éxito el préstamo:", prestamo)
            else:
                print("No se encontró ningún préstamo con el ID proporcionado.")
            conexion.conexion.commit()
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al buscar el préstamo. ", error)
            return None

    def eliminar_prestamo(self):
        try:
            id_prestamo = input("Introduce el ID del préstamo a eliminar: ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "DELETE FROM prestamos WHERE id_prestamo = %s"
            valores = (id_prestamo,)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha eliminado con éxito el préstamo")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al eliminar el préstamo. ", error)
            return None
        

""" 
class MenuPrestamo:
    def __init__(self):
        self.prestamo = Prestamo()

    def mostrar_menu(self):
        print("\n1. Dar de alta un préstamo")
        print("2. Ver todos los préstamos")
        print("3. Modificar un préstamo")
        print("4. Buscar un préstamo")
        print("5. Eliminar un préstamo")
        print("6. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.prestamo.dar_alta()
        elif opcion == 2:
            self.prestamo.ver_prestamos()
        elif opcion == 3:
            id_prestamo = int(input("Introduce el ID del préstamo a modificar: "))
            self.prestamo.modificar(id_prestamo)
        elif opcion == 4:
            self.prestamo.buscar_prestamo()
        elif opcion == 5:
            self.prestamo.eliminar_prestamo()
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

def main():
    menu = MenuPrestamo()
    while True:
        menu.mostrar_menu()
        opcion = int(input("Elige una opción: "))
        menu.ejecutar_opcion(opcion)
        if opcion == 6:
            break

if __name__ == "__main__":
    main()
"""
