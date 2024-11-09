def cargar_lista():
    lista = []
    for i in range(5):
        valor = int(input("ingrese el valor: "))
        lista.append(valor)
    return lista

def mayor_menor(lista):
    numMayor = lista[0]
    numMenor = lista[0]
    for i in range(len(lista)):
        if lista[i] > numMayor:
            numMayor = lista[i]
        
        if lista[i] < numMenor:
            numMenor = lista[i]
    return (numMayor, numMenor)



#bloque principal

lista_uno = cargar_lista()
print(lista_uno)
tupla_uno = mayor_menor(lista_uno)
print(tupla_uno)
numMayor, numMenor = tupla_uno
print("el numero mayor es: ", numMayor)
print("el numero menor es: ", numMenor)