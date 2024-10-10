def carga_valores(num1, num2, num3):
    suma = num1 + num2 + num3
    promedio = suma / 3
    return promedio

#bloque principal

valor1 = int(input("ingrese el primer valor: "))
valor2 = int(input("ingrese el segundo valor: "))
valor3 = int(input("ingrese el tercer valor: "))
print("el promedio es igual a: ",carga_valores(valor1, valor2, valor3))