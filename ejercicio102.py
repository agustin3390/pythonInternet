lista = []
cantElementos = int(input("ingrese el primer valor: "))
subLista = int(input("ingrese el segundo valor: "))
suma = 0
for k in range(cantElementos):
    lista.append([])
    for i in range(subLista):
        valor = int(input("ingrese los valores: "))
        lista[k].append(valor)
print(lista)
for i in range(cantElementos):
    for k in range(subLista):
        suma += lista[i][k]
print(suma)