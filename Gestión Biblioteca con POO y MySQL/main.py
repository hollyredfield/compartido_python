import crud_lector
import crud_libro
import crud_prestamos

lector = crud_lector.Lector(
    nombre="Nombre", 
    apellidos="Apellidos", 
    fecha_alta="FechaAlta", 
    fecha_baja="FechaBaja"
    )

# De anotado la explicación del por qué de estos bloques para futuros proyectos.

# En este bloque, se crea una instancia de la clase Lector del módulo crud_lector. 
# En programación orientada a objetos, el término "instancia" se refiere a la creación de un objeto particular basado en una clase. 
# Una clase es un tipo de dato definido por el programador que encapsula datos y comportamientos asociados. 
# Por lo tanto, cuando creas una instancia de una clase, estás creando un objeto concreto que es una versión específica de esa clase.
# Esta instancia representa a un lector de la biblioteca y se inicializa con valores ficticios (por ejemplo, "Nombre", "Apellidos", "FechaAlta", "FechaBaja"). 
# La creación de esta instancia es necesaria para poder utilizar los métodos de la clase, como alta_lector para dar de alta a un nuevo lector.

# En los siguientes bloques se realiza lo mismo.  

libro = crud_libro.Libro(
    autor="Autor", 
    titulo="Título", 
    genero="Género", 
    paginas="Páginas", 
    anio_publicacion="AñoPublicación", 
    edicion="Edición", 
    idioma="Idioma", 
    ISBN="ISBN", 
    prestamos_realizados="PrestamosRealizados", 
    prestado="Prestado"
    )

prestamos = crud_prestamos.Prestamos(
    fecha_prestamo="FechaPrestamo", 
    libro="Libro", 
    lector="Lector", 
    fecha_devolucion="FechaDevolucion"
    )

# En ambos casos, "libro" y "prestamos" son instancias de las clases Libro y Prestamos, respectivamente. 
# Estas instancias representan objetos concretos (un libro y un préstamo) que pueden interactuar con los métodos y atributos definidos en sus clases correspondientes.
# Las instancias permiten la creación, manipulación y gestión de datos específicos dentro de la lógica de mi programa.

lector.alta_lector("Manolo", "García Castrejón", "1990/07/19")

lector.alta_lector("Silvia", "Castilla Fernandez", "2000/08/20")

libro.alta_libro ("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "365", "1976", "56", "Español", "251F75D258G4", "0", "0")

libro.alta_libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "432", "1967", "25", "Español", "9780061120091", "0", "0")

libro.alta_libro("1984", "George Orwell", "Distopía", "328", "1949", "15", "Inglés", "9780451524935", "0", "0")

prestamos.realizar_prestamo(1,"1991/10/19", 1, 1) # El campo libro y lector de la base de datos está definido como número entero por lo que introduzco el Id de cada uno.

prestamos.realizar_prestamo(2,"2002/06/07", 2, 2)

prestamos.realizar_devolucion(1, "1991/10/19", 1, 1, "1991/11/19")

prestamos.ver_libro_prestado("2002/06/07", 2, 2)

lector.borrar_lector(1)

lector.borrar_lector(2)

libro.borrar_libro(1)

libro.borrar_libro(2)