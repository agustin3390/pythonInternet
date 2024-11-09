def sumar(v1, v2, *v3):
    suma = v1 + v2
    for i in range(len(v3)):
        suma += v3[i]
    return suma


#bloque principal

lista = [1, 2, 3,4,5,6,7,8,9]

print(sumar(*lista))