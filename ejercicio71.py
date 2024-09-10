contador = 0
lista = [120, 10, 200, 34, 500, 70, 7, 101]
for i in range(len(lista)):
    if lista[i] > 100:
        contador += 1
        print("el numero", lista[i], "es mayor a 100")
        continue
    print("el numero", lista[i], "no es mayor a 100")

print("la cantidad de numero mayores a 100 son: ", contador)
