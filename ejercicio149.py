def cargar_empleados():
    lista = []
    for i in range(5):
        nombre = input("ingrese el nombre del empleado: ")
        sueldo = float(input("ingrese el sueldo: "))
        lista.append((nombre,sueldo))
    return lista


def imprimir_lista(lista):
    for nombre,sueldo in lista:
        print("nombre: ", nombre, "sueldo: ", sueldo)


def sueldo_mayor(lista):
    mayor = 0
    nom_mayor = " "
    for nombre,sueldo in lista:
        if sueldo > mayor:
            mayor = sueldo
            nom_mayor = nombre
    print("el sueldo es de: ", nom_mayor)


def sueldos_menores1000(lista):
    contador = 0
    for nombre, sueldo in lista:
        if sueldo < 1000:
            contador += 1
    print("la cantidad de sueldos menor son: ", contador) 

#bloque principal

lista = cargar_empleados()
imprimir_lista(lista)
sueldo_mayor(lista)
sueldos_menores1000(lista)