def cargar():
    diccionario = {}
    continua = "s"
    while continua == "s":
        telefono = int(input("ingrese el numero de telefono: "))
        contacto = input("ingrese el nombre del contacto: ")
        diccionario[contacto] = telefono
        continua = input("desea ingresar otro contacto (s/n)? ")
    return diccionario

def busqueda(diccionario):
    contacto = input("ingrese el nombre del contacto que desea buscar: ")
    if contacto in diccionario:
        diccionario[contacto] = int(input("ingrese el nuevo numero de telefono: "))
    

def imprimir(diccionario):
    for contacto in diccionario:
        print(contacto, diccionario[contacto])

#bloque principal

diccionario = cargar()
busqueda(diccionario)
imprimir(diccionario)