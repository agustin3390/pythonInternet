lista = []
valorMenor = 0
posicion = 0
#cargar de lista..
for i in range(5):
    numEntero = int(input("ingrese un valor: "))
    lista.append(numEntero)
    valorMenor = lista[0]
    if lista[i] < valorMenor:
        valorMenor = lista[i]
        posicion = i

print("lista completa: ", lista)
print("el valor menor es: ", valorMenor)
print("en la posicion: ", posicion)