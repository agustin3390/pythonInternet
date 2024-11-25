def cargar_lista():
    lista = []
    for i in range(5):
        nombre = input("ingrese el nombre: ")
        lista.append(nombre)
    return lista

def ordenar_lista(lista):
    aux = " "
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
        

#bloque principal

lista = cargar_lista()
print(lista)
ordenar_lista(lista)
print(lista)

