"""

Desarrollar un programa que permita gestionar las películas y las funciones en un cine.

Agregar una película: Cada película debe tener un título, director, duración (en minutos) y clasificación (ej. PG, PG-13, PG-18, PG+18).

Visualizar todas las películas: Mostrar una lista de todas las películas disponibles en el cine.

Buscar una película por título o director: Permitir al usuario buscar una película específica.

Eliminar una película: Permitir al usuario eliminar una película de la lista.

"""
cine = [] #Lista vacia en la que se añaden valores introducidos por el usuario

def menu(): #Menu de nuestro programa
    print(f"\n1. Añadir una pelicula")
    print(f"\n2. Visualizar peliculas")
    print(f"\n3. Buscar pelicula")
    print(f"\n4. Eliminar una pelicula")
    print(f"\n5. Salir")
    opcion = int(input(f"\nSelecciona una de las opciones dadas : "))
    return opcion

def anadirpelicula():#Funcion que añade peliculas que el usuario nombra a el archivo cine.txt
    titulo = input(f"\nEscribe el titulo de una pelicula : ")
    director = input(f"\nQuien es el director? : ")
    duracion = input(f"\nCuanto dura? : ")
    clasificacion = input(f"\nEscribe cual es su clasificacion : ")
    try:
        with open("cine.txt","a") as archivo:
            archivo.write(titulo + "," + director + "," + duracion + "," + clasificacion + "\n")
            print(f"\nLa pelicula {titulo} fue añadida correctamente ")
    except FileNotFoundError:
        print(f"\nNo ha sido posible añadir la pelicula ")
    return
   
def visualizarpeliculas():#Funcion que imprime todas las peliculas añadidas a cine.txt en pantalla
    try:
        with open("cine.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                titulo,director,duracion,clasificacion = linea.strip().split(",")
                print(f"Titulo : {titulo} - Director : {director} - Duracion : {duracion} - Clasificacion : {clasificacion}")
    except FileNotFoundError:
        print(f"\nNo hay peliculas disponibles")
    return
              
def buscarpelicula():#Funcion que imprime en pantalla el libro que el usuario escribe y dice si esta disponible o no
    pelicula_a_buscar = input(f"\nDime la pelicula que quieres buscar : ")
    try:
        with open("cine.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if pelicula_a_buscar in linea:
                    print(f"\nLa pelicula {pelicula_a_buscar} esta disponible")          
    except FileNotFoundError:
        print(f"\nLa pelicula {pelicula_a_buscar} no esta disponible")
    return 
    
def eliminarpelicula():#Funcion que elimina una pelicula agregada anteriormente y la almacena en otra lista correspondiente
    pelicula_a_eliminar = input(f"\nDime la pelicula que deseas eliminar : ")
    peliculaseliminadas = []
    eliminado = False
    try:
        with open("cine.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if pelicula_a_eliminar in linea:
                    print(f"\nLa pelicula {pelicula_a_eliminar} ha sido eliminada correctamente ")
                    eliminado = True
                else:
                    peliculaseliminadas.append(linea)
            if eliminado:
                with open("cine.txt","w") as archivo:
                    for linea in peliculaseliminadas:
                        archivo.write(linea)
    except FileNotFoundError:
        print(f"\nNo se a podido eliminar la pelicula") 
    return
