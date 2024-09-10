listaNombres = []
listaNotas = []
#carga de nombre y notas a la lista.
for i in range(5):
    nombreAlumno = input("ingrese el nombre del alumno: ")
    listaNombres.append(nombreAlumno)
    notaAlumno = float(input("ingrese la nota del alumno: "))
    listaNotas.append(notaAlumno)
# ordenmiento por notas de mayor a menor.
for k in range(4):
    for i in range(4-k):
        if listaNotas[i] < listaNotas[i + 1]:
            aux = listaNotas[i]
            listaNotas[i] = listaNotas[i + 1]
            listaNotas[i + 1] = aux
            aux2 = listaNombres[i]
            listaNombres[i] = listaNombres[i + 1]
            listaNombres[i + 1] = aux2
for i in range(5):
    print(listaNombres[i], listaNotas[i])