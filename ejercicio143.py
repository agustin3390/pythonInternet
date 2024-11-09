def cargar_nombre_sueldo():
    nombre = input("ingrese el nombre del empleado: ")
    sueldo = int(input("ingrese el sueldo del empleado: "))
    return (nombre, sueldo)

def sueldo_mejor_pago(empleado1, empleado2):
    nombre_uno, sueldo_uno = empleado1
    nombre_dos, sueldo_dos = empleado2
    if sueldo_uno > sueldo_dos:
        sueldo_mayor = sueldo_uno
    else:
        sueldo_mayor = sueldo_dos
    return sueldo_mayor

#bloque principal

empleado_uno = cargar_nombre_sueldo()
empleado_dos = cargar_nombre_sueldo()

mejor_sueldo = sueldo_mejor_pago(empleado_uno, empleado_dos)
print("el mejor sueldo es: ", mejor_sueldo)