def cargar_lista():
    li = []
    for i in range(5):
        valor = int(input("ingrese un valor: "))
        li.append(valor)
    return li


def imprimir_lista_mayores10(li):
    bandera = 0
    for i in range(len(lista)):
        if lista[i] > 10:
            print(lista[i])
            bandera = 1
    if bandera == 0:
        print("no hay numeros mayores a 10.")



#bloque principal

lista = cargar_lista()
print(lista)
imprimir_lista_mayores10(lista)