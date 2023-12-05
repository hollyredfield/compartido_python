from conexion import Conectar
from libro import Libro
from lector import Lector
#Agregar libro
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
#Agregar lector
conexion = Conectar()
conexion.conexion_bdd()
lector = Lector(conexion)
lector.add_lector("Juan", "Perez", "2021-01-01", "2021-01-01")
conexion.close_connection()
#Ver lectores
conexion = Conectar()
conexion.conexion_bdd()
lector = Lector(conexion)
ver_lectores = lector.ver_lectores()
conexion.close_connection()
#Buscar lector
conexion = Conectar()
conexion.conexion_bdd()
lector = Lector(conexion)
lector.buscar_lector("Juan")
conexion.close_connection()
#Eliminar lector
conexion = Conectar()
conexion.conexion_bdd()
lector = Lector(conexion)
lector.eliminar_lector("Juan")
conexion.close_connection()
#Modificar lector
conexion = Conectar()
conexion.conexion_bdd()
lector = Lector(conexion)
lector.modificar_lector("Juan", "Perez", "2021-01-01", "2021-01-01")
conexion.close_connection()


