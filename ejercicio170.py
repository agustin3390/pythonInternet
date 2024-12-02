import random

def cargar():
    lista = []
    for i in range(10):
        valor = random.randint(1,100)
        lista.append(valor)
    return lista

def rotar_numeros(lista):
    random.shuffle(lista)

def imprimir(lista):
    print(lista)

#bloque principal
lista = cargar()
imprimir(lista)
rotar_numeros(lista)
imprimir(lista)
