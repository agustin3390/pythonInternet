def retorno_caracteres(nombre):
    cant = 0
    for i in range(len(nombre)):
        cant += 1
    return cant

#bloque principal
nomUno = input("ingrese el nombre: ")
contadorUno = retorno_caracteres(nomUno)
nomDos = input("ingrese el segundo nombre: ")
contadorDos = retorno_caracteres(nomDos)
if contadorUno > contadorDos:
    print("el nombre", nomUno, "tiene mayor cantidad de caracteres.")
else:
    print("el nombre", nomDos, "tiene mayor cantidad de caracteres.")