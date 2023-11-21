# Ejemplo de lista: [4, 3, 2, 10, 12, 1, 5, 6]
def insertionSort(arr):
    # Recorremos de 1 a len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Tomamos el primer elemento de la parte sin ordenar
        # Movemos los elementos de arr[0..i-1] que son mayores que key
        # a una posición adelante de su posición actual
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr  # Devolvemos el array ordenado
# Ejemplo de uso
lista = [4, 3, 2, 10, 12, 1, 5, 6]
lista_ordenada = insertionSort(lista)
print(lista_ordenada)
