def cargar():
    productos = {}
    continua = "s"
    while continua == "s":
        codigo = int(input("ingrese el codigo del producto: "))
        descripcion = input("ingrese la descripcion del producto: ")
        stock = int(input("ingrese el stock actual del producto: "))
        productos[codigo] = (codigo,descripcion,stock)
        continua = input("desea ingresar otro producto (s/n)?")
    return productos


def imprimir(productos):
    print("listado de productos..")
    for codigo in productos:
        print(productos[codigo][0],productos[codigo][1], productos[codigo][2])


def consulta_producto(productos):
    codigo = int(input("ingrese el codigo del producto a buscar: "))
    if codigo in productos:
        print(productos[codigo][0], productos[codigo][1], productos[codigo][2])
    else:
        print("no se encuentra ese codigo..")


def stock_cero(productos):
    print("listado de productos con stock 0.")
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(productos[codigo][0], productos[codigo][1])




#bloque principal
productos = cargar()
imprimir(productos)
consulta_producto(productos)
stock_cero(productos)