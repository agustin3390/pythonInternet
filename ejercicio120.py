def lista_mayorMenor(lista):
    numMayor = lista[0]
    numMenor = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > numMayor:
            numMayor = lista[i]
        if lista[i] < numMenor:
            numMenor = lista[i]
    print("el numero mayor es: ", numMayor)
    print("el numero menor es: ", numMenor)

#bloque principal
lista_valores = []
for i in range(5):
    numEntero = int(input("ingrese un numero entero: "))
    lista_valores.append(numEntero)
lista_mayorMenor(lista_valores)