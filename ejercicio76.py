lista = []
suma = 0
for i in range(5):
    sueldo = float(input("ingrese el sueldo del operario: "))
    lista.append(sueldo)
    suma += lista[i]
promedio = suma / len(lista)
print("lista completa")
print(lista)
print("el promedio de sueldos es: ", promedio)