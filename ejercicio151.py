def cargar_productos():
    lista = []
    for i in range(5):
        producto = input("ingrese el nombre del producto: ")
        precio = float(input("ingrese el valor del producto: "))
        lista.append((producto,precio))
    return lista



def imprimir_productos(lista_productos):
    print("lista de productos y precios.")
    for producto,precio in lista_productos:
        print(producto, " ", precio)

def mostar_productos_destacados(lista_productos):
    for elemento in lista_productos:
        if elemento[1] >= 10 and elemento[1] <= 15:
            print(elemento[0])


#bloque principal

lista_productos = cargar_productos()
imprimir_productos(lista_productos)
mostar_productos_destacados(lista_productos)