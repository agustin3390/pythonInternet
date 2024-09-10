listaPaises = []
for i in range(5):
    nombrePais = input("ingrese el nombre del pais: ")
    listaPaises.append(nombrePais)
print("paises desordenados alfabeticamente.")
print(listaPaises)
for k in range(4):
    for i in range(4-k):
        if listaPaises[i] > listaPaises[i + 1]:
            aux = listaPaises[i]
            listaPaises[i] = listaPaises[i + 1]
            listaPaises[i + 1] = aux
print("lista de paises ordenados alfabeticamente")
print(listaPaises)