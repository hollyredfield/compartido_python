# Ejemplo de lista: [10, 7, 8, 9, 1, 5]
def partition(arr, low, high):
    i = (low-1)  # Índice del elemento más pequeño
    pivot = arr[high]  # Pivote
    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            i = i+1  # Incrementamos el índice del elemento más pequeño
            arr[i], arr[j] = arr[j], arr[i]  # Y lo intercambiamos con el elemento en j
    arr[i+1], arr[high] = arr[high], arr[i+1]  # Intercambiamos el pivote con el elemento en i+1
    return (i+1)  # Devolvemos la posición del pivote

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi es la posición del pivote en el array ordenado
        pi = partition(arr, low, high)
        # Ordenamos los elementos antes y después del pivote
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr  # Devolvemos el array ordenado
# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
sorted_arr = quickSort(arr, 0, len(arr)-1)
print("Sorted array:", sorted_arr)