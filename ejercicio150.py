def cargar_lista(cant):
    lista = []
    for i in range(cant):
        palabra = input("ingrese la palabra: ")
        lista.append(palabra)
    return lista

def mostrar_palabras(lista_palabras):
    for elemento in lista_palabras:
        if len(elemento) > 5:
            print(elemento)
    

#bloque principal
cant = int(input("ingrese la cantidad de palabras a cargar: "))
lista_palabras = cargar_lista(cant)
mostrar_palabras(lista_palabras)