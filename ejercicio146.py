def carga_datosEmpleado():
    lista = []
    for i in range(5):
        nombre = input("ingrese el nombre: ")
        mes1 = float(input("ingrese el sueldo del primer mes: "))
        mes2 = float(input("ingrese el sueldo del segundo mes: "))
        mes3 = float(input("ingrese el sueldo del tercer mes: "))
        lista.append([nombre,(mes1,mes2,mes3)])
    return lista

def montoTotal_empleado(lista):
    lista_sumas = []
    for i in range(len(lista)):
        suma = lista[i][1][0] + lista[i][1][1] + lista[i][1][2]
        lista_sumas.append(suma)
    for i in range(len(lista)):
        print( lista[i][0],":", lista_sumas[i])
    return lista_sumas

def mostrar_sueldosMayor10000(lista_empleado, lista_suma):
    print("empleados con sueldos mayores a 10000")
    for i in range(len(lista_empleado)):
        if lista_suma[i] > 10000:
            print(lista_empleados[i][0])

#bloque principal

lista_empleados = carga_datosEmpleado()
print(lista_empleados)
lista_suma = montoTotal_empleado(lista_empleados)
mostrar_sueldosMayor10000(lista_empleados, lista_suma)
