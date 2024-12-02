def cargar():
    lista = []
    for i in range(5):
        palabra = input("ingrese una palabra: ")
        lista.append(palabra)
    return lista

def mostrar(lista):
    aux = lista[0]
    lista[0] = lista[-1]
    lista[-1] = aux
    print(lista)

#bloque principal
lista = cargar()
mostrar(lista)
