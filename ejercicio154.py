def cargar_diccionario():
    diccionario = {}
    for i in range(4):
        clave = int(input("ingrese el numero de documento: "))
        nombre = input("ingrese el nombre de la persona: ")
        diccionario[clave] = nombre
    return diccionario

def imprimir(diccionario):
    print("listado de dni y nombre de las personas.")
    for clave in diccionario:
        print(clave, diccionario[clave])


def mostrar_nombre(diccionario):
    contador = 0
    dni_Abuscar = int(input("ingrese el dni que desea encontrar"))
    if dni_Abuscar in diccionario:
        print(diccionario[dni_Abuscar])        
    else:
        print("no se encontro el dni ingresado.")

#bloque principal

diccionario = cargar_diccionario()
imprimir(diccionario)
mostrar_nombre(diccionario)