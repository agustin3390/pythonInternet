def cargar_lista():
    lista_uno = []
    for i in range(10):
        numEntero = int(input("ingrese un numero entero: "))
        lista_uno.append(numEntero)
    return lista_uno


def numeros_positivos_negativos(lista_uno):
    lista_positivos = []
    lista_negativos = []
    for i in range(len(lista_uno)):
        if lista_uno[i] >= 0:
            lista_positivos.append(lista_uno[i])
        else:
            lista_negativos.append(lista_uno[i])
    return [lista_positivos,lista_negativos]



#bloque principal

lista_principal = cargar_lista()
li_positivos, li_negativos = numeros_positivos_negativos(lista_principal)
print(li_positivos)
print(li_negativos)