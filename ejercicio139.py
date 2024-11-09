def edades(v1, *lista):
    cantidad = 0
    if v1 >= 18:
        cantidad += 1
    for i in range(len(lista)):
        if lista[i] >= 18:
            cantidad += 1
    return cantidad



#blqoue

lista = [20, 15, 30, 12, 11, 50, 45, 23, 8]
edad = 35
print(edades(edad, *lista))