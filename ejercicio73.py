contador = 0
lista = ["mariano", "esteban", "juan", "lucas", "raul"]
for i in range(len(lista)):
    if len(lista[i]) >= 5:
        contador += 1

print("la cantidad de nombres que tiene mayores carecteres que 5 son: ", contador) 
