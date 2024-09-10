listaSueldos = []
cantEmpleados = int(input("ingrese la cantidad de empleados: "))
for i in range(cantEmpleados):
    sueldoEmpleado = int(input("ingrese el sueldo del empleado: "))
    listaSueldos.append(sueldoEmpleado)
print("lista de sueldos")
print(listaSueldos)
for k in range(cantEmpleados - 1):
    for i in range(cantEmpleados - 1 - k):
        if listaSueldos[i] > listaSueldos[i + 1]:
            aux = listaSueldos[i]
            listaSueldos[i] = listaSueldos[i + 1]
            listaSueldos[i + 1] = aux
print("lista de sueldos ordenadas.")
print(listaSueldos)