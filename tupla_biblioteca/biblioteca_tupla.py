"""
Eres el encargado de una biblioteca y 
necesitas gestionar la información de los libros disponibles.
Cada libro se representa mediante una tupla que contiene: 
(ID, Título, Autor, Año de Publicación). El ID ha de ser autoincremental
Tu tarea es desarrollar un programa en Python que permita: 
El usuario debe proporcionar el título, autor y año de publicación. 
El ID debe generarse automáticamente y ser único. 
Mostrar toda la información de cada libro en un formato legible. 
El usuario proporciona un ID y el programa muestra la información del libro 
correspondiente 
o un mensaje indicando que el libro no se encuentra. 
El usuario proporciona un ID y el programa elimina el libro correspondiente 
o muestra un mensaje indicando que el libro no se encuentra.
Utiliza una lista para almacenar todas las tuplas de libros.
Implementa funciones para cada una de las operaciones: 
añadir, listar, buscar y eliminar.
Asegúrate de manejar posibles errores, 
como intentar eliminar un libro que no existe. 
"""
#crear una tupla por cada libro que vaya a añadir, dentro, cada tupla alberga ID, título
#autor, año de publicación
#Crear una lista de libros, con las tuplas vacía:lista_libros[]
#meter id automático/incremental
#nuevoid = len(lista_libros) +1
#se crea una lista vacía que albergue los libros que vaya introduciendo el usuario
#Para añadir un libro, se le pide al usuario en una función añadir libros con input y se le añade a la lista.
#Se crea una función que añada de forma automática el ID a cada libro que el usuario añada
#Se crea otra función para indexar por ID el libro que pida el usuario y que muestre el libro que es.
#Se usa otra función para listar los libros de la biblioteca: mostrar todos los libros. 
#Se crea otra función para que el usuario si coje un libro de la lista, se elimine de la lista.

listalibro=[]
#Opciones que elija el usuario.

def menu():
    print("1. Añadir Libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    opcion= input("Elige una opción: ")
    return (int(opcion))
    
def anadirlibro(listalibro):
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    año = input("Introduce el año del libro: ")
    
    id = len(listalibro) +1 
    libro = ( id, titulo, autor, año)
    listalibro.append(libro)
    print(f"Libro añadido con ID {id}")
def listarlibros(listalibro):
    for libro in listalibro:
        print(f"ID: {libro[0]}, titulo:{libro[1]}, autor:{libro[2]}, año:{libro[3]} ")
    return listalibro
def buscarlibro(id, listalibro):
    
    id_buscar = int(input("Ingrese el ID del libro a buscar: "))
    encontrado = False
    for libro in listalibro:
        if libro[0] == id_buscar:
            print(f"ID: {libro[0]}, título: {libro[1]}, autor: {libro[2]}, año: {libro[3]}")
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado")

def eliminarlibro(listalibro):
    id_eliminar = int(input("Dime el ID que deseas eliminar: "))
    eliminado = False

    for libro in listalibro:
        if libro[0] == id_eliminar:
            print("Libro eliminado")
            listalibro.remove(libro)
            eliminado = True
            break

    if not eliminado:
        print("Libro no encontrado")


while True:
    option = menu()
    if option == 1:
        anadir = anadirlibro(listalibro)
    elif option == 2:
        listar = listarlibros(listalibro)
    elif option == 3:
        buscar = buscarlibro(id, listalibro)
    elif option == 4:
        eliminar = eliminarlibro(listalibro)
    elif option == 5:
        print("Gracias por usar el programa. ")
        break
        
    
                
                
            
    



    
    
