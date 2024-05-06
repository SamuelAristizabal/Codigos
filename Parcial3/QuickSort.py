'''
https://www.youtube.com/watch?v=c4TVqJIl67c
'''
#Este algoritmo tiene una profundidad de recursión igual a la longitud de la lista, por lo que si se toma como pivote al primer elemento entonces para listas superiores a 1000 se desencadena un RecursionError
import random

def separacion(lista):
    if len(lista) < 1:
        return []
    
    izquierda = []
    derecha = []
    pivote = lista.pop(random.randint(0, len(lista) - 1)) #Escoge un número random entre la longitud de la lista y lo escoge para ser un pivote

    for i in lista: #Se usa un proceso similar a los árboles, colocando a la izquierda a los valores menores al pivote y a la derecha los valores mayores
        if i < pivote:
            izquierda.append(i)
        else:
            derecha.append(i)

    return izquierda, pivote, derecha

def quickSort(lista):
    if len(lista) < 2:
        return lista
    
    izquierda, pivote, derecha = separacion(lista) #Separa la lista

    return quickSort(izquierda) + [pivote] + quickSort(derecha) #Concatena la lista
