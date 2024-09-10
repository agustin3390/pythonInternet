contador = 0
oracion = input("escribir una oracion. \n")
oracion2 = oracion.lower()
for i in range(len(oracion2)):
    if oracion2[i] == 'a' or oracion2[i] == 'e' or oracion2[i] == 'i' or oracion2[i] == 'o' or oracion2[i] == 'u':
        contador += 1


print("la cantidad de vocales son: ", contador)