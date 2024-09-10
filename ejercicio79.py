lista = []
valorAlto = 0
for i in range(5):
    numEntero = int(input("ingrese un numero: "))
    lista.append(numEntero)
    if lista[i] > valorAlto:
        valorAlto = lista[i]
print("lista completa: ", lista)
print("el valor mas alto:  ", valorAlto)