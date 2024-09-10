lista = []
#carga la lista.
for i in range(5):
    numEntero = int(input("ingrese un valor entero: "))
    lista.append(numEntero)
print("lista de elementos enteros")
print(lista)
# lista de mayor a menor.
for k in range(4):
    for i in range(4-k):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
print("lista oordenada de menor a mayor.")
print(lista)
for k in range(4):
    for i in range(4-k):
        if lista[i]<lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
print("lista ordenada de mayor a menor.")
print(lista)