contador = 0
oracion = input("escriba una oracion. \n")
for i in range(len(oracion)):
    if oracion[i] == " ":
        contador += 1
print("la cantidad de espacio en blanco son: ", contador)