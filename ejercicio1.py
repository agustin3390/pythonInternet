nombreUno = str(input("ingrese el nombre de la persona: "))
edadUno = int(input("ingrese la edad de la primer persona"))
alturaUno = float(input("ingrese la altura de la primer persona"))
nombreDos = str(input("ingrese el nombre de la persona: "))
edadDos = int(input("ingrese la edad de la segunda persona"))
alturaDos = float(input("ingrese la altura de la segunda persona"))

if edadUno > edadDos:
    print("el mas grande es: ", nombreUno )
else:
    print("el mas grade es: ", nombreDos)
