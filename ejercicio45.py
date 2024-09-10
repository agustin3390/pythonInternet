supMayores = 0
cantTriangulos = int(input("ingrese la cantidad de triangulos: "))
for i in range(cantTriangulos):
    base = int(input("ingrese la base del triangulo: "))
    altura = int(input("ingrese la altura del triangulo: "))
    superficie = (base * altura)// 2
    if superficie > 12:
        supMayores = supMayores + 1

    print("la base es: ", base)
    print("la altura es: ", altura)
    print("la superficie es: ", superficie)

print("la cantidad de superficies mayores a 12 son: ", supMayores)
