lista = []
contador = 0
for k in range(50):
    lista.append([])
    contador += 1
    valor = 1
    for i in range(contador):
        lista[k].append(valor)
        valor += 1

for i in range(50):
    print(lista[i])