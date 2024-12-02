import random

def cargar():
    lista = []
    for i in range(4):
        valor = random.randint(1,3)
        lista.append(valor)
    lista.append(1)
    return lista

def imprimir(lista):
    print(lista)

def mostra_uno(lista):
    while lista[0] != 1:
        random.shuffle(lista)

#bloque principal

lista = cargar()
imprimir(lista)
mostra_uno(lista)
imprimir(lista)