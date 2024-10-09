def calculo_superficie(lado1):
    superficie = lado1 * lado1
    return superficie

def calculo_perimetro(lado1):
    perimetro = lado1 * 4
    return perimetro

def super_primetr(lado1):
    respuesta = input("ingrese si desea saber el primetro o la superficie del cuadrado: ")
    if respuesta == 'superficie':
        superficie = calculo_superficie(lado1)
        print("la superficie es igual a : ", superficie)
    elif respuesta == 'perimetro':
        perimetro = calculo_perimetro(lado1)
        print("el perimetro es igual a : ",perimetro)
    else:
        print("la respuesta es incorrecta..")


#bloque principal

valorUno = int(input("ingrese el lado de un cuadrado: "))
super_primetr(valorUno)
