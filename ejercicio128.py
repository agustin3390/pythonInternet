def cargarNombresEdades():
    liEdad = []
    liNombres = []
    for i in range(5):
        nombre = input("ingrese el nombre de la persona: ")
        liNombres.append(nombre)
        edad = int(input("ingrese la edad de la persona: "))
        liEdad.append(edad)
    return [liNombres,liEdad]


def personas_mayores_edad(liNombres,liEdad):
    for i in range(len(liEdad)):
        if liEdad[i] >= 18:
            print(liNombres[i])


def imprimir_promedio_edad(liEdad):
    suma = 0
    for i in range(len(liEdad)):
        suma += liEdad[i]
    promedio = suma / len(liEdad)
    print("el promedio es: ", promedio)



#bloque principal

listaNombres, listaEdades = cargarNombresEdades()
personas_mayores_edad(listaNombres, listaEdades)
imprimir_promedio_edad(listaEdades)
