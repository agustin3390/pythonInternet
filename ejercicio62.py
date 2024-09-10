nombre = input("ingrese un nombre en minuscula: ")
if nombre[0] == 'a' or nombre[0] == 'e' or nombre[0] == 'i' or nombre[0] == 'o' or nombre[0] == 'u':
    print("el nombre", nombre, "empieza con una vocal.")
else:
    print("el nombre",nombre, "empieza con una consonante.")