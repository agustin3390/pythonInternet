def contador_vocales(palabra):
    contador = 0
    variableMinuscula = palabra.lower()
    for i in range(len(variableMinuscula)):
        if variableMinuscula[i] == 'a' or variableMinuscula[i] == 'e' or variableMinuscula[i] == 'i' or variableMinuscula[i] == 'o' or variableMinuscula[i] == 'u':
            contador += 1
    return contador

#bloque principal


cantLetras = contador_vocales('hola mundo')
print(cantLetras)
cantLetras = contador_vocales('agustin gerlero')
print(cantLetras)
cantLetras = contador_vocales('sabrina asquini')
print(cantLetras)
