from lectores import Lector
from libros import Libro
from prestamos import Prestamo

class Menu:
    def __init__(self):
        self.lector = Lector()
        self.libro = Libro()
        self.prestamo = Prestamo()

    def mostrar_menu(self):
        print("\n1. Dar de alta un lector")
        print("2. Ver lectores")
        print("3. Modificar lector")
        print("4. Eliminar lector")
        print("5. Buscar lector")
        print("6. Dar de alta un libro")
        print("7. Ver todos los libros")
        print("8. Modificar un libro")
        print("9. Buscar un libro")
        print("10. Eliminar un libro")
        print("11. Dar de alta un préstamo")
        print("12. Ver todos los préstamos")
        print("13. Modificar un préstamo")
        print("14. Buscar un préstamo")
        print("15. Eliminar un préstamo")
        print("16. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion in range(1, 6):
            self.ejecutar_opcion_lector(opcion)
        elif opcion in range(6, 11):
            self.ejecutar_opcion_libro(opcion - 5)
        elif opcion in range(11, 16):
            self.ejecutar_opcion_prestamo(opcion - 10)
        elif opcion == 16:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 16.")

    def ejecutar_opcion_lector(self, opcion):
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

    def ejecutar_opcion_libro(self, opcion):
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

    def ejecutar_opcion_prestamo(self, opcion):
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

def main():
    menu = Menu()
    while True:
        menu.mostrar_menu()
        opcion = int(input("Elige una opción: "))
        menu.ejecutar_opcion(opcion)
        if opcion == 16:
            break

if __name__ == "__main__":
    main()