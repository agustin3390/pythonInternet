def cargar_diccionario():
    productos = {}
    for i in range(5):
        articulo = input("ingrese el nombre del producto: ")
        precio = int(input("ingrese el precio del producto: "))
        productos[articulo] = precio
    return productos


def imprimir_productos(productos):
    for articulo in productos:
        print(articulo, productos[articulo])


def imprimir_mayores100(productos):
    for articulo in productos:
        if productos[articulo] > 100:
            print(articulo)

#bloque principal

productos = cargar_diccionario()
imprimir_productos(productos)
imprimir_mayores100(productos)
