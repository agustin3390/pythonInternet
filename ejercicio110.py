lista = []
for i in range(5):
    numEntero = int(input("ingrese los numeros: "))
    lista.append(numEntero)

print(lista)
posicion = 0
while posicion < lista[posicion]:
    if lista[posicion] >= 10:
        lista.pop(posicion)
    else:
        posicion += 1
print(lista)