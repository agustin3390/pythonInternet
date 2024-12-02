def capicua(cadena):
    iguales = 0
    indice = -1
    for i in range(len(cadena)//2):
        if cadena[i] == cadena[indice]:
            iguales += 1
        indice -= 1
    print(cadena)
    if len(cadena)//2 == iguales:
        print("es capicua..")
    else:
        print("no es capicua..")



#bloque principal

capicua("menem")
capicua("osvaldo")
capicua("neuquen")