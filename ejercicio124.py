
def palabrasConMasLetras(listaPalabras):
    cantMayor = len(listaPalabras[0])
    pos = 0
    for i in range(len(listaPalabras)):
        if len(listaPalabras[i]) > cantMayor:
            cantMayor = len(listaPalabras[i])
            pos = i
    return listaPalabras[pos]






#bloque principal
listaPalabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
cantLetras = palabrasConMasLetras(listaPalabras)
print("la palabra con mayor letras es: ", cantLetras)