def cargar():
    lista = []
    for i in range(5):
        valor = int(input("ingrese el valor: "))
        lista.append(valor)
    return lista


def numero_mayor(lista):
    mayor = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    print("el numero mayor es: ", mayor)


def sumar(lista):
    suma = 0
    for elementos in lista:
        suma += elementos
    print("la suma es igual a:", suma)