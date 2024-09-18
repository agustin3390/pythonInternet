nombres = []
sueldos = []
totalSueldos = []
suma = 0
for i in range(3):
    nombre = input("ingrese el nombre del empleado: ")
    nombres.append(nombre)
    
    sueldoEmpleado1 = int(input("ingrese el sueldo del empleado: "))
    sueldoEmpleado2 = int(input("ingrese el sueldo del empleado: "))
    sueldoEmpleado3 = int(input("ingrese el sueldo del empleado: "))
    sueldos.append([sueldoEmpleado1, sueldoEmpleado2,sueldoEmpleado3])
    suma = sueldoEmpleado1 + sueldoEmpleado2 + sueldoEmpleado3
    totalSueldos.append(suma)
sueldoMayor = totalSueldos[0]
nombreMayor = nombres[0]
for i in range(3):
    print(nombres[i], totalSueldos[i])
    print(sueldos[i])

for i in range(3):
    if totalSueldos[i] > sueldoMayor:
        sueldoMayor = totalSueldos[i]
        nombreMayor = nombres[i]
print("el empleado con mayor sueldo es: ", nombreMayor)