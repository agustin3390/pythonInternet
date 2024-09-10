nombreUno = input("ingrese el primer nombre: ")
nombreDos = input("ingrese el segundo nombre: ")
if nombreUno > nombreDos:
    print("el nombre ", nombreUno, "es mayor alfabeticamente")
elif nombreDos > nombreUno:
    print("el nombre ", nombreDos, "es mayor alfabeticamente")
else:
    print("los nombres son iguales")