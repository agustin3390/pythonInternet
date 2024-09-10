numMayores = 0
numIguales = 0
cantValores = int(input("ingrese la cantidad de valores: "))
for i in range(0,cantValores,1):
    numEntero = int(input("ingrese el numero. \n"))
    if numEntero > 1000:
        numMayores = numMayores + 1
    elif numEntero == 1000:
        numIguales = numIguales + 1

print("la cantidad de numeros iguales son: ", numIguales)
print("la cantidad de numeros mayores son: ", numMayores)
