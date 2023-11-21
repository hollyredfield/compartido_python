# Ejemplo de lista: [64, 25, 12, 22, 11, 90]
def selectionSort(arr):
    # Recorremos todos los elementos del array
    for i in range(len(arr)):
        # Encontramos el mínimo elemento en el array sin ordenar
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Intercambiamos el elemento mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  # Devolvemos el array ordenado
# Ejemplo de lista
lista = [64, 25, 12, 22, 11, 90]

# Ordenamos la lista utilizando el algoritmo de selección
lista_ordenada = selectionSort(lista)

# Imprimimos la lista ordenada
print(lista_ordenada)