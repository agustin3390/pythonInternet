def sumar(v1, v2, *lista):
    suma = v1 + v2
    for i in range(len(lista)):
        suma += lista[i]
    return suma



#bloque principal

print(sumar(1,2,5,7,8,9,1))
print(sumar(1,4,5))
print(sumar(1,2))