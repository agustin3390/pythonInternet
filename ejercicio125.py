def retorno_producto(lista):
    producto = lista[0]
    for i in range(1,len(lista)):
        producto = producto * lista[i]
    return producto



#bloque principal

lista = [10,20,30,40,50]

producto = retorno_producto(lista)
print("el producto es: ", producto)