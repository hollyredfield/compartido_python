from conexion import Conexion
import mysql.connector

class Lector:
    def __init__(self, nombre=None, apellidos=None, fecha_alta=None, fecha_baja=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def set_fecha_alta(self, fecha_alta):
        self.fecha_alta = fecha_alta
    def get_fecha_alta(self):
        return self.fecha_alta 
    def set_fecha_baja(self, fecha_baja):
        self.fecha_baja = fecha_baja
    def get_fecha_baja(self):
        return self.fecha_baja
    def dar_alta(self):
        try:
            nombre = input("Introduce el nombre: ")
            apellidos = input("Introduce los apellidos: ")
            fecha_alta = input("Introduce la fecha de alta (formato MM/DD/YYYY): ") #año-mes-día
            fecha_baja = input("Introduce la fecha de baja (formato MM/DD/YYYY): ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "Insert into lectores (nombre, apellidos, fecha_alta, fecha_baja) VALUES (%s, %s, %s, %s)"
            valores = (nombre, apellidos, fecha_alta, fecha_baja)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha dado de alta con éxito el lector")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al añadir el lector. ", error)
            return None
    def ver_lectores(self):
        try:
            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "select * from lectores"
            cursor.execute(query)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al ver los lectores. ", error)
            return None
    def modificar_lector(self, id_lector):
        try:
            nombre = input("Introduce el nuevo nombre: ")
            apellidos = input("Introduce los nuevos apellidos: ")
            fecha_alta = input("Introduce la nueva fecha de alta (formato MM/DD/YYYY): ")
            fecha_baja = input("Introduce la nueva fecha de baja (formato MM/DD/YYYY): ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "UPDATE lectores SET nombre = %s, apellidos = %s, fecha_alta = %s, fecha_baja = %s WHERE id = %s"
            valores = (nombre, apellidos, fecha_alta, fecha_baja, id_lector)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha modificado con éxito el lector")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al modificar el lector. ", error)
            return None
    def eliminar_lector(self):
        try:
            id_lector = input("Introduce el ID del lector a eliminar: ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "DELETE FROM lectores WHERE id_lector = %s"
            valores = (id_lector,)
            cursor.execute(query, valores)
            conexion.conexion.commit()
            print("Se ha eliminado con éxito el lector")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al eliminar el lector. ", error)
            return None
    def buscar_lector(self):
        try:
            id_lector = input("Introduce el ID del lector a buscar: ")

            conexion = Conexion()
            conexion.conexion_bdd()
            cursor = conexion.conexion.cursor()
            query = "SELECT * FROM lectores WHERE id_lector = %s"
            valores = (id_lector,)
            cursor.execute(query, valores)
            registro = cursor.fetchone()
            if registro is not None:
                print(registro)
            else:
                print("No se encontró ningún lector con el ID proporcionado.")
            conexion.cerrar_conexion_bdd()
        except mysql.connector.Error as error:
            print("Error al buscar el lector. ", error)
            return None

#peter.modificar_lector(1) #se pone el id en el paréntesis que se quiere modificar
#peter.eliminar_lector()

""" 
class Menu:
    def __init__(self):
        self.lector = Lector()

    def mostrar_menu(self):
        print("\n1. Dar de alta un lector")
        print("2. Ver lectores")
        print("3. Modificar lector")
        print("4. Eliminar lector")
        print("5. buscar")
        print("6.")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.lector.dar_alta()
        elif opcion == 2:
            self.lector.ver_lectores()
        elif opcion == 3:
            id_lector = input("Introduce el ID del lector a modificar: ")
            self.lector.modificar_lector(id_lector)
        elif opcion == 4:
            self.lector.eliminar_lector()
        elif opcion == 5:
            self.lector.buscar_lector()
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

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
