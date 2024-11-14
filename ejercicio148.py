def cargar_lista():
    lista = []
    for i in range(5):
        valor = int(input("ingrese el valor: "))
        lista.append(valor)
    return lista

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

def mayor_lista(lista):
    mayor = 0
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    print("el mayor elemento es: ",mayor)


def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    print("la suma es: ",suma)

#bloque principal
lista = cargar_lista()
imprimir_lista(lista)
mayor_lista(lista)
suma_lista(lista)