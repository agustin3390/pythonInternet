listaAlumnos = []
listaNotas = []
#carga los elementos de la lista
for i in range(3):
    alumno = input("ingrese el nombre del alumno: ")
    listaAlumnos.append(alumno)
    nota1 = int(input("ingrese la primer nota del alumno: "))
    nota2 = int(input("ingrese la segunda nota del alumno: "))
    listaNotas.append([nota1,nota2])
for i in range(3):
    print("alumno:", listaAlumnos[i], "nota 1:", listaNotas[i][0], "nota 2:", listaNotas[i][1])