def multiplicar_lista(lista, num1):
    lista_multiplicar = []
    for i in range(len(lista)):
        multiplicar = lista[i] * num1
        lista_multiplicar.append(multiplicar)

    print(lista)
    print(lista_multiplicar)



#bloque principal

lista = [1,15,30,22,4,8]
numEntero = int(input("ingrese un numero entero: "))
multiplicar_lista(lista, numEntero)
    