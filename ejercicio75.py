lista = []
bandera = 1
while (bandera == 1):
    numEntero = int(input("ingrese el numero: "))
    if numEntero != 0:
        lista.append(numEntero)
    else:
        bandera = 0
print("tamaño de lista: ", len(lista))
print("lista completa")
print(lista)