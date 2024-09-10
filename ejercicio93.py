listaPaises = []
listaHabitantes = []
#carga de paises y cant de habitanes a las listas.
for i in range(5):
    pais = input("ingrese el nombre del pais: ")
    listaPaises.append(pais)
    habitantes = int(input("ingrese la cantidad de habitantes: "))
    listaHabitantes.append(habitantes)
#ordenamient de paises alfabeticamente.
for k in range(4):
    for i in range(4-k):
        if listaPaises[i] > listaPaises[i + 1]:
            aux = listaPaises[i]
            listaPaises[i] = listaPaises[i + 1]
            listaPaises[i + 1] = aux
            aux2 = listaHabitantes[i]
            listaHabitantes[i] = listaHabitantes[i + 1]
            listaHabitantes[i + 1] = aux2
#muestra paises ordenados alfabeticamente.
for i in range(5):
    print(listaPaises[i], listaHabitantes[i])

#ordenamiento por cant de habitantes.
for k in range(4):
    for i in range(4-k):
        if listaHabitantes[i] < listaHabitantes[i + 1]:
            aux = listaHabitantes[i]
            listaHabitantes[i] = listaHabitantes[i + 1]
            listaHabitantes[i + 1] = aux
            aux2 = listaPaises[i]
            listaPaises[i] = listaPaises[i + 1]
            listaPaises[i + 1] = aux2

#lista ordenada por cantidad de habitantes.
for i in range(5):
    print(listaPaises[i], listaHabitantes[i])
