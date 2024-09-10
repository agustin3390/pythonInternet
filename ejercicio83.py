listaNOmbre = []
listaEdad = []
#carga de nombres y edades.
for i in range(5):
    nombre = input("ingrese el nombre de la persona: ")
    listaNOmbre.append(nombre)
    edad = int(input("ingrese la edad de la persona: "))
    listaEdad.append(edad)

#recorremos la lista para ver los mayores de edad.
for i in range(5):
    if listaEdad[i] >= 18:
        print("nombre: ", listaNOmbre[i])
        print("edad: ", listaEdad[i])