def tabla_multiplicar(valor1, termino = 10):
    for i in range(1, termino + 1):
        producto = valor1 * i
        print(producto, end = "-")



#bloque principla

valor1 = int(input("ingrese un valor: "))
tabla_multiplicar(termino = 8, valor1 = 15)