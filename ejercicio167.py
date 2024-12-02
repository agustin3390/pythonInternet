def cargar_cadena():
    cadena = input("ingrese una palabra: ")
    return cadena

def mostar_cadena(cadena):
    indice = -1
    for i in range(len(cadena)):
        print(cadena[indice], end="")
        indice -= 1


#bloque principal
cadena = cargar_cadena()
print(cadena)
mostar_cadena(cadena)
