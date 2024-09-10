listaUno = []
listaDos = []
listaSuma = []
for i in range(4):
    numUno = int(input("ingrese el valor de la lista uno: "))
    listaUno.append(numUno)
    numDos = int(input("ingrese el valor de la lista dos: "))
    listaDos.append(numDos)
    suma = listaUno[i] + listaDos[i]
    listaSuma.append(suma)
print("lista uno: ", listaUno)
print("lista dos: ", listaDos)
print("lista suma: ", listaSuma)
