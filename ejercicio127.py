def cargar_lista():
    li = []
    for i in range(5):
        valor = int(input("ingrese un valor: "))
        li.append(valor)
    return li


def numeros_mayores_menores(li):
    li2 = []
    numMayor = li[0]
    numMenor = li[0]
    for i in range(len(li)):
        if li[i] > numMayor:
            numMayor = li[i]
    li2.append(numMayor)
    for i in range(len(li)):
        if li[i] < numMenor:
            numMenor = li[i]
    li2.append(numMenor)
    return li2




#bloque principal

lista = cargar_lista()
print(lista)
lista_dos = numeros_mayores_menores(lista)
print("el numero mayor es: ", lista_dos[0])
print("el numero menor es: ", lista_dos[1])