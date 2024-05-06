def left(i): # Encuentra el índice del hijo izquierdo
    return 2*i + 1

def right(i): # Encuentra el índice del hijo derecho
    return 2*i + 2

def parent(i): # Encuentra el índice del nodo padre
    return (i - 1) // 2

def max_heapify(a, heap_size, i): #Se usa para mantener la condición de max heap, se asume que los sub árboles son max heaps
    l = left(i)
    r = right(i)

    largest = i

    #Intercambia el a[i] con el mayor de sus hijos
    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r
    
    if largest != i:
        # swap elements
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)

def build_max_heap(a): #Hace un max heap desde un arreglo desordenado
    heap_size = len(a)

    for i in range(len(a) // 2 - 1, -1, -1): #Recorre desde el último nodo del árbol hasta la raíz
        max_heapify(a, heap_size, i)

def heapSort(a):
    build_max_heap(a) #Convierte el arreglo en un max heap

    for i in range(len(a) - 1, 0, -1): #Intervambia el primer elemento con el último elemento del heap y reduce el tamaño del heap en 1 (retira el mayor valor)
        # "swap elements"
        a[i], a[0] = a[0], a[i]

        # "after the swap the last element is now sorted, but the new root may break the max-heap condition"
        # "fix it by calling max-heapify with a smaller heap size (sorted elements are out of the picture)"
        max_heapify(a, i, 0)

    return a
