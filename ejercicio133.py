def retorno_suma(num1, num2, num3 = 10, num4 = 30, num5 = 80):
    suma = num1 + num2 + num3 + num4 + num5
    return suma




#bloque principal

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
suma_enteros = retorno_suma(num1, num2)
print("la suma es: ", suma_enteros)