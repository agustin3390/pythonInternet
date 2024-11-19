def imprimir_diccionario(paises):
    for clave in paises:
        print(clave, " ", paises[clave])




#bloque principal
paises = {"argentina": 10000, "brasil": 30000, "peru": 5000, "uruguay": 1000}
imprimir_diccionario(paises)