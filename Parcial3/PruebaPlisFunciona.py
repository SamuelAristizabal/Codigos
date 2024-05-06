import random
import time
import matplotlib.pyplot as plt
from MergeSort import mergeSort
from CountingSort import countingSort
from HeapSort import heapSort
from QuickSort import quickSort
from Listas import *

def medir_tiempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fin = time.time()
    return fin - inicio

if __name__ == "__main__":
    algoritmos = {
        'Counting Sort': countingSort,
        'Heap Sort': heapSort,
        'Merge Sort': mergeSort,
        'Quick Sort': quickSort,
    }
    
    tamaños = [10, 100, 1000, 10000, 100000, 1000000]
    eficiencias = {nombre: [] for nombre in algoritmos}
    
    for tamaño in tamaños:
        lista = listaRandom(tamaño, 1, 10000000)
        for nombre, algoritmo in algoritmos.items():
            tiempo = medir_tiempo(algoritmo, lista.copy())
            eficiencias[nombre].append(tiempo)

    # Generar gráficas
    for nombre, tiempos in eficiencias.items():
        plt.plot(tamaños, tiempos, label=nombre)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Eficiencia temporal de algoritmos de ordenación')
    plt.legend()
    plt.show()
