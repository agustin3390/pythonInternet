cantEmpleados = int(input("ingrese la cantidad de empleados: "))
listaNombre = []
listaSueldo = []
for i in range(cantEmpleados):
    nombre = input("ingrese el nombre del empleado: ")
    listaNombre.append(nombre)
    sueldo = float(input("ingrese el sueldo del empleado: "))
    listaSueldo.append(sueldo)
print(listaNombre)
print(listaSueldo)

posicion = 0
while posicion < len(listaSueldo):
    if listaSueldo[posicion] >= 1000:
        listaNombre.pop(posicion)
        listaSueldo.pop(posicion)
    else:
        posicion += 1
print(listaNombre)
print(listaSueldo)