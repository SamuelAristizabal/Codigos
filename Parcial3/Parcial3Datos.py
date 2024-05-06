'''
/ bubblesort NO
/mergesort
/countingsort
/heapsort
/quicksort
/bucketsort NO
'''

import random
import time
from MergeSort import mergeSort
from CountingSort import countingSort
from HeapSort import heapSort
from QuickSort import quickSort
#from BucketSort import bucketSort
#from BubbleSort import bubbleSort
from Listas import *
    
if __name__ == "__main__":

    contador = 0
    tamaños = []
    tiempos = []
    while (contador < 3):
        if contador == 0:
            print("####################### Lista Random #######################")
            #Crear las listas aleatorias con los mismos valores para cada algoritmo
            lista10 = listaRandom(10, 1, 100)
            lista100 = listaRandom(100,1,1000)
            lista1000 = listaRandom(1000,1,10000)
            lista10000 = listaRandom(10000,1,100000)
            lista100000 = listaRandom(100000,1,1000000)
            lista1000000 = listaRandom(1000000,1,10000000)
            
        elif contador == 1:
            print("####################### Lista Ascendente #######################")
            #Crear las listas aleatorias con los mismos valores para cada algoritmo
            lista10 = listaAscendente(10, 1, 100)
            lista100 = listaAscendente(100,1,1000)
            lista1000 = listaAscendente(1000,1,10000)
            lista10000 = listaAscendente(10000,1,100000)
            lista100000 = listaAscendente(100000,1,1000000)
            lista1000000 = listaAscendente(1000000,1,10000000)
        
        elif contador == 2:
            print("####################### Lista Descendente #######################")
            #Crear las listas aleatorias con los mismos valores para cada algoritmo
            lista10 = listaDescendente(10, 1, 100)
            lista100 = listaDescendente(100,1,1000)
            lista1000 = listaDescendente(1000,1,10000)
            lista10000 = listaDescendente(10000,1,100000)
            lista100000 = listaDescendente(100000,1,1000000)
            lista1000000 = listaDescendente(1000000,1,10000000)
        '''
        elif contador == 3:
            print("####################### Lista Decimal #######################")
            #Crear las listas aleatorias con los mismos valores para cada algoritmo
            lista10 = listaDecimal(10)
            lista100 = listaDecimal(100)
            lista1000 = listaDecimal(1000)
            lista10000 = listaDecimal(10000)
            lista100000 = listaDecimal(100000)
            lista1000000 = listaDecimal(1000000)
        '''

        
        print("***************** Ordenamiento Counting Sort *****************")
        print("Con lista de longitud 10")
        inicio = time.time()
        lista_ordenada = countingSort(lista10)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        print(lista_ordenada)

        print("Con lista de longitud 100")
        inicio = time.time()
        lista_ordenada = countingSort(lista100)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000")
        inicio = time.time()
        lista_ordenada = countingSort(lista1000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 10000")
        inicio = time.time()
        lista_ordenada = countingSort(lista10000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 100000")
        inicio = time.time()
        lista_ordenada = countingSort(lista100000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000000")
        inicio = time.time()
        lista_ordenada = countingSort(lista1000000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)
        print()


        print("***************** Ordenamiento Heap Sort *****************")
        print("Con lista de longitud 10")
        inicio = time.time()
        lista_ordenada = heapSort(lista10)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        print(lista_ordenada)

        print("Con lista de longitud 100")
        inicio = time.time()
        lista_ordenada = heapSort(lista100)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000")
        inicio = time.time()
        lista_ordenada = heapSort(lista1000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 10000")
        inicio = time.time()
        lista_ordenada = heapSort(lista10000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 100000")
        inicio = time.time()
        lista_ordenada = heapSort(lista100000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000000")
        inicio = time.time()
        lista_ordenada = heapSort(lista1000000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)
        print()

        print("***************** Ordenamiento Merge Sort *****************")
        print("Con lista de longitud 10")
        inicio = time.time()
        lista_ordenada = mergeSort(lista10)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        print(lista_ordenada)

        print("Con lista de longitud 100")
        inicio = time.time()
        lista_ordenada = mergeSort(lista100)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000")
        inicio = time.time()
        lista_ordenada = mergeSort(lista1000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 10000")
        inicio = time.time()
        lista_ordenada = mergeSort(lista10000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 100000")
        inicio = time.time()
        lista_ordenada = mergeSort(lista100000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000000")
        inicio = time.time()
        lista_ordenada = mergeSort(lista1000000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)
        print()


        print("***************** Ordenamiento Quick Sort *****************")
        print("Con lista de longitud 10")
        inicio = time.time()
        lista_ordenada = quickSort(lista10)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        print(lista_ordenada)

        print("Con lista de longitud 100")
        inicio = time.time()
        lista_ordenada = quickSort(lista100)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000")
        inicio = time.time()
        lista_ordenada = quickSort(lista1000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 10000")
        inicio = time.time()
        lista_ordenada = quickSort(lista10000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 100000")
        inicio = time.time()
        lista_ordenada = quickSort(lista100000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000000")
        inicio = time.time()
        lista_ordenada = quickSort(lista1000000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)
        print()

        contador += 1
    #Este algoritmo está hecho para arreglar valores entre 0 y 1 ordenados uniformemente
    '''
        print("***************** Ordenamiento Bucket Sort *****************")
        print("Con lista de longitud 10")
        inicio = time.time()
        lista_ordenada = bucketSort(lista10)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        print(lista_ordenada)

        print("Con lista de longitud 100")
        inicio = time.time()
        lista_ordenada = bucketSort(lista100)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000")
        inicio = time.time()
        lista_ordenada = bucketSort(lista1000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 10000")
        inicio = time.time()
        lista_ordenada = bucketSort(lista10000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 100000")
        inicio = time.time()
        lista_ordenada = bucketSort(lista100000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000000")
        inicio = time.time()
        lista_ordenada = bucketSort(lista1000000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)
        print()
    '''


    #Este algoritmo requiere una cantidad exagerada de tiempo para poder ordenar una gran cantidad de números
    '''
        print("***************** Ordenamiento Bubble Sort *****************")
        print("Con lista de longitud 10")
        inicio = time.time()
        lista_ordenada = bubbleSort(lista10)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        print(lista_ordenada)

        print("Con lista de longitud 100")
        inicio = time.time()
        lista_ordenada = bubbleSort(lista100)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000")
        inicio = time.time()
        lista_ordenada = bubbleSort(lista1000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 10000")
        inicio = time.time()
        lista_ordenada = bubbleSort(lista10000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 100000")
        inicio = time.time()
        lista_ordenada = bubbleSort(lista100000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)

        print("Con lista de longitud 1000000")
        inicio = time.time()
        lista_ordenada = bubbleSort(lista1000000)
        fin = time.time()
        print("Tiempo de ejecucion = {:.30f}".format(fin - inicio))
        #print(lista_ordenada)
        print()
    '''
    