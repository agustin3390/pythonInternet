lista = []
for i in range(5):
    numEntero = int(input("ingrese un numero entero: "))
    lista.append(numEntero)
print(lista)
print("---------------------")
print(lista.pop(0))
print(lista.pop(1))
print(lista.pop(2))

print("-------------------------")
print(lista)