listaSueldos = []
for i in range(5):
    sueldo = float(input("ingrese los sueldos: "))
    listaSueldos.append(sueldo)
print("lista de sueldos")
print(listaSueldos)
for i in range(4):
    if listaSueldos[i] > listaSueldos[i + 1]:
        aux = listaSueldos[i]
        listaSueldos[i] = listaSueldos[i + 1]
        listaSueldos[i + 1] = aux

print("lista de sueldos con el mayor atras")
print(listaSueldos)