listaProducto = []
listaPrecio = []
for i in range(5):
    descricionProducto = input("ingrese el nombre del producto: ")
    listaProducto.append(descricionProducto)
    precioProducto = float(input("ingrese el precio"))
    listaPrecio.append(precioProducto)
    precioReferencia = listaPrecio[0]
print("precio de referencia: $", precioReferencia)
for i in range(5):
    if listaPrecio[i] > precioReferencia:
        print("producto: ",listaProducto[i])
        print("precio: $", listaPrecio[i])