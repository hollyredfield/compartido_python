""" 
Identificaremos las entidades principales que necesitamos:
Libro: Representa un libro en la biblioteca.
Usuario: Representa a un usuario de la biblioteca.
Biblioteca: Gestiona los libros y usuarios. 
"""
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False


    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False


    def devolver(self):
        self.prestado = False
        
""" 
Aquí, Libro encapsula propiedades como titulo, autor, y isbn. Los métodos prestar y devolver cambian el estado del libro 
(abstracción y encapsulamiento).
Clase Usuario 
"""

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []


    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False


    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver() g
            self.libros_prestados.remove(libro)
            return True
        return False
    
""" 
La clase Usuario gestiona los libros prestados a cada usuario, demostrando encapsulamiento y abstracción.
Clase Biblioteca 
"""

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []


    def agregar_libro(self, libro):
        self.libros.append(libro)


    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)


    def prestar_libro(self, isbn, identificacion):
        libro = next((libro for libro in self.libros if libro.isbn == isbn and not libro.prestado), None)
        usuario = next((usuario for usuario in self.usuarios if usuario.identificacion == identificacion), None)
        
        if libro and usuario:
            return usuario.tomar_prestado(libro)
        return False
    
"""
Paso 4: Demostración del Uso de la Aplicación
Crearemos algunos libros y usuarios y realizaremos operaciones de préstamo. 
"""

# Creando libros y usuarios
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "123456789")
libro2 = Libro("1984", "George Orwell", "987654321")


usuario1 = Usuario("Ana Pérez", "001")
usuario2 = Usuario("Luis Martínez", "002")


biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)


# Prestar un libro
biblioteca.prestar_libro("123456789", "001")


# Intentar prestar el mismo libro a otro usuario
resultado = biblioteca.prestar_libro("123456789", "002")  # Esto debería fallar, ya que el libro está prestado


# Devolver el libro
usuario1.devolver_libro(libro1)
