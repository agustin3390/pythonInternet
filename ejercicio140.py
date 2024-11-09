def cargar_tupla():
    dia = int(input("ingrese el dia: "))
    mes = int(input("ingrese el mes: "))
    año = int(input("ingrese el año: "))
    return (dia,mes,año)

def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")


#blqoue

fecha = cargar_tupla()
imprimir_fecha(fecha)
lista = list(fecha)
print(lista)