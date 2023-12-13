from lectores import Lector
from libros import Libro
from prestamos import Prestamo

class Menu:
    def __init__(self):
        self.lector = Lector()
        self.libro = Libro()
        self.prestamo = Prestamo()

    def mostrar_menu(self):
        print("""
        1. Dar de alta un lector
        2. Ver lectores
        3. Modificar lector
        4. Eliminar lector
        5. Buscar lector
        6. Dar de alta un libro
        7. Ver todos los libros
        8. Modificar un libro
        9. Buscar un libro
        10. Eliminar un libro
        11. Dar de alta un préstamo
        12. Ver todos los préstamos
        13. Modificar un préstamo
        14. Buscar un préstamo
        15. Eliminar un préstamo
        16. Salir
        """)

    def ejecutar_opcion(self, opcion):
        opciones_lector = {
            1: self.lector.dar_alta,
            2: self.lector.ver_lectores,
            3: lambda: self.lector.modificar_lector(input("Introduce el ID del lector a modificar: ")),
            4: self.lector.eliminar_lector,
            5: self.lector.buscar_lector,
        }

        opciones_libro = {
            1: self.libro.dar_alta,
            2: self.libro.ver_libros,
            3: lambda: self.libro.modificar(int(input("Introduce el ID del libro a modificar: "))),
            4: self.libro.buscar_libro,
            5: self.libro.eliminar_libro,
        }

        opciones_prestamo = {
            1: self.prestamo.dar_alta,
            2: self.prestamo.ver_prestamos,
            3: lambda: self.prestamo.modificar(int(input("Introduce el ID del préstamo a modificar: "))),
            4: self.prestamo.buscar_prestamo,
            5: self.prestamo.eliminar_prestamo,
        }

        if opcion in range(1, 6):
            opciones_lector[opcion]()
        elif opcion in range(6, 11):
            opciones_libro[opcion - 5]()
        elif opcion in range(11, 16):
            opciones_prestamo[opcion - 10]()
        elif opcion == 16:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 16.")


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
