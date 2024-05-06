def countingSort(lista):
    
    maximo = lista[0] #Toma el valor inicial de la lista como número máximo
    minimo = lista[0] #Lo mismo que el anterior pero en mínimo
    for num in lista:
        if num > maximo: #Se recorre la lista y se determina los rangos de la misma
            maximo = num
        if num < minimo:
            minimo = num
    
    rango = maximo - minimo + 1 #Se establece el rango

    # Según el rango anterior se crea una lista del tamaño del rango de números llena de ceros
    contador = [0] * rango

    
    for num in lista: # Llena el arreglo de conteo con la frecuencia de cada elemento
        contador[num - minimo] += 1

    
    ordenada = []
    for i in range(rango): # Reconstruye el arreglo ordenado
        ordenada.extend([i + minimo] * contador[i])

    return ordenada