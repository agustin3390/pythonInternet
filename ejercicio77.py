promedioMayor = 0
promedioMenor = 0
lista = []
suma = 0
#se almacenan y se suman las alturas..
for i in range(5): 
    altura = float(input("ingrese la altura: "))
    lista.append(altura)
    suma += lista[i]
promedio = suma / len(lista)
#se comparan las alturas con el promedio...
for j in range(len(lista)): 
    if lista[j] >= promedio:
        promedioMayor += 1
    else:
        promedioMenor += 1
print("lista completa: ", lista)
print("promedio: ", promedio)
print("la cantidad de mayores al promedio son: ", promedioMayor)
print("la cantidad de menores al promedio son: ", promedioMenor)