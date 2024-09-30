listaEmpleados = []
listaDiasFaltados = []
nomMenosFaltas = ""
for i in range(3):
    nombre = input("ingrese el nombre del empleado: ")
    listaEmpleados.append(nombre)
    listaDiasFaltados.append([])
    cantDiasFaltados = int(input("ingrese la cantidad de dias faltados"))
    for j in range(cantDiasFaltados):
        diaFaltado = int(input("ingrese la fecha del dia que falto: "))
        listaDiasFaltados[i].append(diaFaltado)
menosFaltas = len(listaDiasFaltados[0])
for i in range(3):
    print("nombre:",listaEmpleados[i],"\n")
    print("fecha de faltas:",listaDiasFaltados[i],"\n")
    print("cantidad de inasistencias: ", len(listaDiasFaltados[i]),"\n")
    print("--------------------------------------------\n")

for i in range(3):
    if len(listaDiasFaltados[i])< menosFaltas:
        menosFaltas = len(listaDiasFaltados[i])
for i in range(3):
    if len(listaDiasFaltados[i]) == menosFaltas:
        print(listaEmpleados[i])