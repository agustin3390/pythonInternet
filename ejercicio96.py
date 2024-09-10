lista = [[10],[20,30],[30,40,50],[60,70,80,90],[100,110,120,130,140]]
suma = 0
for k in range(len(lista)):
    for i in range(len(lista[k])):
        suma += lista[k][i]
print("la suma es igual a: ", suma)