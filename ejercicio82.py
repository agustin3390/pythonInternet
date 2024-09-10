contador = 0
lista = []
aux = 0
numMayor = 0
#carga de numeros enteros
for i in range(5):
    numEntero = int(input("ingrese el valor: "))
    lista.append(numEntero)
    numMayor = lista[0]
    if lista[i] > numMayor:
        numMayor = lista[i]
for j in range(5):
    if lista[j] == numMayor:
        contador += 1

print("el numero mayor es: ", numMayor)
if contador >= 2:
    print("hay mas de dos numeros mayores iguales")
