def cargar():
    empleados = {}
    continua = "s"
    while continua == "s":
        legajo = int(input("ingrese el numero de legajo del empleado: "))
        lista = []
        nombre = input("ingrese el nombre del empleado: ")
        lista.append(nombre)
        profesion = input("ingrese la profesion del empleado: ")
        lista.append(profesion)
        sueldo = float(input("ingrese el sueldo: "))
        lista.append(sueldo)
        empleados[legajo] = lista
        continua = input("desea ingresar otro empleado (s/n)? ")
    return empleados


def buscar_empleado(empleados):
    legajo = int(input("ingrese el numero de legajo que desea buscar: "))
    if legajo in empleados:
        empleados[legajo][2] = float(input("ingrese el nuevo sueldo: "))
    else:
        print("el legajo no existe..")


def empleados_profesion(empleados):
    print("lista de empleados analistas en sistemas..")
    for legajo in empleados:
        if empleados[legajo][1] == "analista en sistemas":
            print(empleados[legajo][0], empleados[legajo][2])

#bloque principal

empleados = cargar()
buscar_empleado(empleados)
empleados_profesion(empleados)