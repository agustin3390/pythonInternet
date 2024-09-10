listaM = []
listaT = []
for i in range(8):
    print(i)
    sueldo = float(input("ingrese el sueldo: "))
    if i < 4:
        listaM.append(sueldo)
    else:
        listaT.append(sueldo)

print("sueldos del turno mañana: ", listaM)
print("sueldos del turno tarde: ", listaT)