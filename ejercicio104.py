listaPaises = []
listaTemperaturas = []
temperaturaMedia = []
nombreMayor = ""
for i in range(4):
    pais = input("ingrese el nombre del pais: ")
    listaPaises.append(pais)
    listaTemperaturas.append([])
    for j in range(3):
        temperatura = int(input("ingrese la temperatura mensual: "))
        listaTemperaturas[i].append(temperatura)

for i in range(4):
    print(listaPaises[i])
    print(listaTemperaturas[i])
    print("------------------------")

for i in range(4):
    suma = 0
    for j in range(3):
        suma += listaTemperaturas[i][j]
    media = suma / 3
    temperaturaMedia.append(media)

for i in range(4):
    print("la temperatura media trimestral de", listaPaises[i], "es de:", temperaturaMedia[i],"\n")
temMayor = temperaturaMedia[0]
for i in range(4):
    if temperaturaMedia[i] > temMayor:
        temMayor = temperaturaMedia[i]
        nombreMayor = listaPaises[i]

print("el pais con mayor temperatura trimestral es:", nombreMayor)