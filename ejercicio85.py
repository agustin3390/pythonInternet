listaNombres = []
listaNotas = []
contador = 0
for i in range(4):
    nombreAlumno = input("ingrese el nombre del alumno: ")
    listaNombres.append(nombreAlumno)
    notaAlumno = float(input("ingrese la nota del alumno: "))
    listaNotas.append(notaAlumno)
for i in range(4):
    if listaNotas[i] >= 8:
        print("nombre:", listaNombres[i])
        print("nota:", listaNotas[i])
        print("condicion de nota: MUY BUENO.")
        contador += 1
    elif listaNotas[i] >= 4:
        print("nombre:", listaNombres[i])
        print("nota:", listaNotas[i])
        print("condicion de nota: BUENO.")
    else:
        print("nombre:", listaNombres[i])
        print("nota:", listaNotas[i])
        print("condicion de nota: INSUFICIENTE.")

print("la cantidad de alumnos con promedio superior o igual a 8 son:", contador)