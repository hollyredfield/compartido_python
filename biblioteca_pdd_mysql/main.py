from conexion import Conectar
from libro import Libro
#Agregar libro
""" 
conect = Conectar()
conect.conexion_bdd()
libro = Libro(conect)
libro.add_book("Harry Potter", "J.K. Rowling", "Fantasia", 1000, 1997, 1, "Español", "123456789", 0, False)
conect.close_connection()
#Ver libros
conect = Conectar()
conect.conexion_bdd()
libro = Libro(conect)
ver_libros = libro.ver_libros()
conect.close_connection()
print(ver_libros)
#Buscar libro
conect = Conectar()
conect.conexion_bdd()
libro = Libro(conect)
libro.buscar_libro("Harry Potter")
conect.close_connection()
#Eliminar libro
conexion = Conectar()
conexion.conexion_bdd()
libro = Libro(conexion)
libro.eliminar_libro("Harry Potter")
conexion.close_connection()
#Modificar libro
conexion = Conectar()
conexion.conexion_bdd()
libro = Libro(conexion)
libro.modificar_libro("Harry Potter", "J.K. Rowling", "Fantasia", 1000, 1997, 1, "Español", "123456789", 0, False)
conexion.close_connection()
#Prestar libro
conexion = Conectar()
conexion.conexion_bdd()
libro = Libro(conexion)
libro.prestra_libro("Harry Potter")
conexion.close_connection()
#Devolver libro
conexion = Conectar()
conexion.conexion_bdd()
libro = Libro(conexion)
libro.devolver_libro("Harry Potter")
conexion.close_connection() 
"""

def menu():
    while True:
        print("1. Añadir libro")
        print("2. Ver Libros")
        print("3. Buscar Libro")
        print("4. Eliminar Libro")
        print("5. Modificar Libro")
        print("6. Prestar Libro")
        print("7. Devolver Libro")
        print("8. Salir")
        choice = input("Elige de forma numérica : ")

        conexion = Conectar()
        conexion.conexion_bdd()
        libro = Libro(conexion)

        if choice == '1':
            libro.add_book("Harry Potter", "J.K. Rowling", "Fantasia", 1000, 1997, 1, "Español", "123456789", 0, False)
        elif choice == '2':
            ver_libros = libro.ver_libros()
            print(ver_libros)
        elif choice == '3':
            libro.buscar_libro("Harry Potter")
        elif choice == '4':
            libro.eliminar_libro("Harry Potter")
        elif choice == '5':
            libro.modificar_libro("Harry Potter", "J.K. Rowling", "Fantasia", 1000, 1997, 1, "Español", "123456789", 0, False)
        elif choice == '6':
            libro.prestra_libro("Harry Potter")
        elif choice == '7':
            libro.devolver_libro("Harry Potter")
        elif choice == '8':
            print("Hasta pronto, deseamos que vuelvas pronto.")
            break
            
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")

        conexion.close_connection()

menu()