Ejemplodelista: [64, 34, 25, 12, 22, 11, 90]
def bubbleSort(arr):
    n = len(arr)  # Obtenemos la longitud del array
    # Recorremos todos los elementos del array
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorremos el array desde 0 hasta n-i-1
            # Intercambiamos si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Devolvemos el array ordenado
# Ejemplo de uso
ejemplo_lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubbleSort(ejemplo_lista)
print("Lista original:", ejemplo_lista)
print("Lista ordenada:", lista_ordenada)