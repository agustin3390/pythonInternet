listaSueldos = []
for i in range(5):
    sueldo = int(input("ingrese el sueldo: "))
    listaSueldos.append(sueldo)
print("lista normal")
print(listaSueldos)
for k in range(4):
    for i in range(4-k):
        if listaSueldos[i] > listaSueldos[i + 1]:
            aux = listaSueldos[i]
            listaSueldos[i] = listaSueldos[i + 1]
            listaSueldos[i + 1] = aux
print("lista de sueldos ordenada de menor a mayor.")
print(listaSueldos)