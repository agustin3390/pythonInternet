import random

print("Quien adina el numero en menos tiros...")
numero_correcto = random.randint(1,100)
num_alternativo = -1
contador = 0
while numero_correcto != num_alternativo:
    num_alternativo = int(input("ingrese un numero del 1 al 100: "))
    if num_alternativo == numero_correcto:
        print("gano")
    else:
        if num_alternativo > numero_correcto:
            print("el numero aleatorio es menor.")
        else:
            print("el numero aleatorio es mayor. ")
    contador += 1
print("cantidad de intentos: ", contador)