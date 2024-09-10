respuesta = "si"
suma = 0
while respuesta == "si" or respuesta != "no":
    numEntero = int(input("ingrese el numero: "))
    suma += numEntero
    respuesta = input("desea ingresar otro valor: ")

print("la suma es igual a: ", suma)