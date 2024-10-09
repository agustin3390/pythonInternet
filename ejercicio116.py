
def numero_mayor(num1, num2, num3):
    mayor = 0
    if num1 > num2 and num1 > num3:
       mayor = num1
    elif num2 > num3:
        mayor = num2
    else:
        mayor = num3
    return mayor

def carga_valores(num1, num2, num3):
    valor1 = int(input("ingrese el primer valor: "))
    valor2 = int(input("ingrese el segundo valor: "))
    valor3 = int(input("ingrese el tercer valor: "))
    mayorNumero = numero_mayor(valor1, valor2, valor3)
    print("el numero mayor es: ", mayorNumero)



#bloque principal
valor1 = 0
valor2 = 0
valor3 = 0
carga_valores(valor1, valor2, valor3)
