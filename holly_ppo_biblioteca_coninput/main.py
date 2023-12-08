from conexion import Conectar
from libro import Libro
from lector import Lector
from prestamos import Prestamo

def main():
    while True:
        print("\n1. Agregar libro")
        print("2. Ver libros")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Modificar libro")
        print("6. Prestar libro")
        print("7. Devolver libro")
        print("8. Agregar lector")
        print("9. Ver lectores")
        print("10. Buscar lector")
        print("11. Eliminar lector")
        print("12. Modificar lector")
        print("13. Añadir préstamo")
        print("14. Ver préstamos")
        print("15. Buscar préstamo")
        print("16. Eliminar préstamo")
        print("17. Modificar préstamo")
        print("18. Salir")
        opcion = int(input("\nSeleccione una opción: "))

        conexion = Conectar()
        conexion.conexion_bdd()

        if opcion == 1:
            libro = Libro(conexion)
            libro.add_book()
        elif opcion == 2:
            libro = Libro(conexion)
            ver_libros = libro.ver_libros()
            print(ver_libros)
        elif opcion == 3:
            libro = Libro(conexion)
            libro.buscar_libro()
        elif opcion == 4:
            libro = Libro(conexion)
            libro.eliminar_libro()
        elif opcion == 5:
            libro = Libro(conexion)
            libro.modificar_libro()
        elif opcion == 6:
            libro = Libro(conexion)
            libro.prestra_libro()
        elif opcion == 7:
            libro = Libro(conexion)
            libro.devolver_libro()
        elif opcion == 8:
            lector = Lector(conexion)
            lector.add_lector()
        elif opcion == 9:
            lector = Lector(conexion)
            ver_lectores = lector.ver_lectores()
            print(ver_lectores)
        elif opcion == 10:
            lector = Lector(conexion)
            lector.buscar_lector()
        elif opcion == 11:
            lector = Lector(conexion)
            lector.eliminar_lector()
        elif opcion == 12:
            lector = Lector(conexion)
            lector.modificar_lector()
        elif opcion == 13:
            prestamo = Prestamo(conexion)
            prestamo.add_prestamo()
        elif opcion == 14:
            prestamo = Prestamo(conexion)
            prestamo.ver_prestamos()
        elif opcion == 15:
            prestamo = Prestamo(conexion)
            prestamo.buscar_prestamo()
        elif opcion == 16:
            prestamo = Prestamo(conexion)
            prestamo.eliminar_prestamo()
        elif opcion == 17:
            prestamo = Prestamo(conexion)
            prestamo.modificar_prestamo()
        elif opcion == 18:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        conexion.close_connection()

if __name__ == "__main__":
    main()