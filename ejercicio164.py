def cargar():
    lista = []
    for i in range(10):
        numEntero = int(input("ingrese el numero:"))
        lista.append(numEntero)
    return lista

def mitad_lista(lista):
    return lista[:5]


#bloque principal 
lista = cargar()
for i in range(5):
    lista2 = mitad_lista(lista)
print(lista)
print(lista2)