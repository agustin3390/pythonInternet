listaPadres = []
listaHijos = []
for k in range(3):
    listaHijos.append([])
    padre1 = input("ingrese el nombre del padre: ")
    padre2 = input("ingrese el nombre de la madre: ")
    listaPadres.append([padre1, padre2])
    cantHijos = int(input("ingrese la cantidade de hijos: "))
    for i in range(cantHijos):
        hijos = input("ingrese el nombre del hijo: ")
        listaHijos[k].append(hijos)

print(listaPadres)
print(listaHijos)