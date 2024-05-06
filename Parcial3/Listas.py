import random
def listaRandom(n, min_val=1, max_val= 10000):
    # Se verifica si el rango de valores es suficiente para n elementos únicos
    if max_val - min_val + 1 < n:
        print("El rango de valores no es suficiente")
        return None

    #Se hace una lista que no repite valores
    lista = random.sample(range(min_val, max_val+1), n)
    return lista

#El código no corre si se hacen listas decimales, ni con los algoritmos que teóricamente deberían poder ordenarlos
'''
def listaDecimal(n):
    numeros = set()
    while len(numeros) < n:
        num = round(random.uniform(0, 1), 3)  # genera un número aleatorio entre 0 y 1 con 3 decimales
        numeros.add(num)
    return list(numeros)
'''

def listaAscendente(n, numInferior = 1, numSuperior = 100):
    lista = [random.randint(numInferior, numSuperior) for _ in range(n)]
    lista.sort() #Se usa la función sort solo para tener unos datos base
    return lista

def listaDescendente(n, numInferior = 1, numSuperior = 100):
    lista = [random.randint(numInferior, numSuperior) for _ in range(n)]
    lista.sort(reverse = True)
    return lista