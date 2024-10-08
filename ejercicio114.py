def numero_menor():
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    num3 = int(input("ingrese el tercer valor: "))
    if num1 < num2 and num1 < num3:
        print("el numero menor es: ", num1)
    elif num2 < num1 and num2 < num3:
        print("el numero menor es: ", num2)
    else:
        print("el numero menor es: ", num3)


#bloque principal

numero_menor()
numero_menor()