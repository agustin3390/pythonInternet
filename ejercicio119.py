def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def lista_mayorNumero(lista):
    numMayor = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > numMayor:
            numMayor = lista[i]
    return numMayor

def lista_menorNumero(lista):
    numMenor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < numMenor:
            numMenor = lista[i]
    return numMenor




#bloque principal
lista_valores = [10, 20, 30, 40, 50]
print(lista_valores)
print("la suma de la la lista es: ", suma_lista(lista_valores))
print("el numero mayor es: ", lista_mayorNumero(lista_valores))
print("el numero menor es: ", lista_menorNumero(lista_valores))