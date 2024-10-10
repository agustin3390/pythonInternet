def retonar_superficie(lado):
    sup = lado * lado
    return sup

#bloque principal

la = int(input("ingrese el lado del cuadrado: "))
print("la superficie es igual a: ",retonar_superficie(la))
if retonar_superficie(la) == 100:
    print("el valor es igual a 100.")
else:
    print("es diferente de 100")