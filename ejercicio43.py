multiplo5 = 0
multiplo3 = 0
for i in range(15):
    numEntero = int(input("ingrese el numero "))
    if numEntero % 3 == 0:
        multiplo3 = multiplo3 + 1
    
    if numEntero % 5 == 0:
        multiplo5 = multiplo5 + 1

print("la cantidad de valores multiplo de 3 son: ", multiplo3)
print("la cantidad de valores multiplo de 5 son: ", multiplo5)

