# Ejemplo de lista: [12, 11, 13, 5, 6, 7]
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2  # Encontramos el punto medio del array
        L = arr[:mid]  # Dividimos el array en dos mitades
        R = arr[mid:]
        mergeSort(L)  # Ordenamos la primera mitad
        mergeSort(R)  # Ordenamos la segunda mitad
        i = j = k = 0
        # Copiamos los datos a los arrays temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        # Comprobamos si quedan elementos
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr  # Devolvemos el array ordenado
# Ejemplo de lista desordenada
arr = [12, 11, 13, 5, 6, 7]

# Ordenamos la lista utilizando el algoritmo merge sort
sorted_arr = mergeSort(arr)

# Imprimimos la lista ordenada
print(sorted_arr)