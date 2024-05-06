'''
https://www.youtube.com/watch?v=r-YA7LD_nD0
'''

def merge(list1, list2):
    result = []
    # Indices para las listas
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Si list1 se termina
    if i == len(list1):
        for k in range(j, len(list2)):
            result.append(list2[k]) #agrega todos los elementos de la segunda sublista si se acaba el arreglo
    if j == len(list2):
        for k in range(i, len(list1)):
            result.append(list1[k])
    return result

def mergeSort(lista): #Divide la lista en dos sublistas para arreglarlas cada una por su lado usando recursividad
    if len(lista) < 2:
        return lista
    else:
        mitad = (len(lista))//2
        lista1 = mergeSort(lista[:mitad])
        lista2 = mergeSort(lista[mitad:])
        return merge(lista1,lista2)

    