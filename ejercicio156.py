def cargar():
    continua = "s"
    agenda = {}
    while continua == "s":
        fecha = input("ingrese la fecha del evento: ej(x/xx/x):")
        hora = input("ingrese la hora del evento: ")
        actividad = input("ingrese la actividad que se realiza: ")
        agenda[fecha] = [(hora, actividad)]
        continua = input("desea ingresar otra activdad (s/n)?")
    return agenda


def imprimir_listado(agenda):
    print("listado completo..")
    for fecha in agenda:
        print(fecha, agenda[fecha][0][0], agenda[fecha][0][1])


def consulta_fecha(agenda):
    fecha = input("ingrese la fecha del evento: ")
    if fecha in agenda:
        print(agenda[fecha][0][0], agenda[fecha][0][1])

#bloque principal

agenda = cargar()
imprimir_listado(agenda)
consulta_fecha(agenda)