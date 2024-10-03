#falta terminar...
lista = []
for i in range(10):
    numEntero = int(input("ingrese el numero: "))
    lista.append(numEntero)
print(lista)
posicion = 0

while posicion < len(lista):
    if lista[posicion] == 5:
        lista.pop(posicion)
    else:
        posicion += 1
print(lista)