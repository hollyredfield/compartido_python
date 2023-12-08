class Libro:
        def __init__(self, autor, titulo, genero, paginas, anio_publicacion, edicion, idioma, isbn, prestamos_realizados, editorial, id_libro):
            self.autor= autor
            self.titulo = titulo
            self.genero = genero
            self.paginas = paginas
            self.anio_publicacion = anio_publicacion
            self.edicion = edicion 
            self.idioma = idioma 
            self.isbn = isbn
            self.prestamos_realizados = prestamos_realizados
            self.prestado = False
            self.editorial = editorial
            self.devolver = False
            self.id_libro = id_libro
            
        def visualizarlibro(self):
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Género: {self.genero}")
            print(f"Edición:{self.edicion}")
            print(f"ISBN: {self.isbn}")
            print(f"Editorial: {self.editorial}")
            
        def buscarlibro(self, titulo, autor):
            if self.titulo == titulo or self.autor == autor or self.genero == genero or self.edicion == edicion or self.isbn == isbn:
                return True
            return False
        
        def eliminarlibro(self, titulo, id_libro):
            if self.titulo == titulo or self.titulo == titulo or self.id_libro == id_libro:
                return True
            return False
        
        def prestar(self):
            if not self.prestado:
                self.prestado = True
                return True
            return False
        
        def devuelto(self):
            self.prestado = False