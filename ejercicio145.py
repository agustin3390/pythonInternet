def cargar_lista():
    paises = []
    for i in range(5):
        pais = input("ingrese el nombre del pais: ")
        cantidad = int(input("ingrese la cantidad de habitantes: "))
        paises.append((pais,cantidad))
    return paises

def mostrar_lista(paises):
    for i in range(len(paises)):
        print("pais: ", paises[i][0])
        print("cant habitantes: ", paises[i][1])


def paises_mayorPoblacion(paises):
    pos = 0
    for i in range(1, len(paises)):
        if paises[i][1] > paises[pos][1]:
            pos = i
    print("el pais con mayor cantidad de habitantes es: ", paises[pos][0])


#bloque principal

lista_paises = cargar_lista()
mostrar_lista(lista_paises)
paises_mayorPoblacion(lista_paises)