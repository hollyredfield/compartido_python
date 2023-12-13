from bdd_clientes import *
from crud import *
def menu():
    print("1. Añadir cliente")
    print("2. Ver clientes")
    print("3. Eliminar cliente")
    print("4. Buscar cliente")
    print("5. Modificar cliente")
    print("6. Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            anadir_cliente()
        elif opcion == 2:
            ver_clientes()
        elif opcion == 3:
            eliminar_cliente()
        elif opcion == 4:
            buscar_cliente()
        elif opcion == 5:
            modificar_cliente()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

if __name__ == "__main__":
    main()