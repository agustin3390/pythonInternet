def cargar_listas():
    li_nombres = []
    li_precios = []
    for i in range(5):
        nombre = input("ingrese el nombre del articulo: ")
        li_nombres.append(nombre)
        precio = float(input("ingrese el precio del articulo: "))
        li_precios.append(precio)
    return [li_nombres,li_precios]

def imprimir_nombres_precios(li_nombres,li_precios):
    for i in range(len(li_precios)):
        print("nombre: ",li_nombres[i], "precio: ", li_precios[i])

def articulo_mayor_precio(li_nombres, li_precios):
    articuloMayor = lista_precios[0]
    nombreMayor = lista_nombres[0]
    for i in range(len(li_precios)):
         if li_precios[i] > articuloMayor:
              articuloMayor = li_precios[i]
              nombreMayor = li_nombres[i]
    return nombreMayor


def articulos_menores(li_nombres, li_precios):
    precio_usuario = float(input("ingrese el precio que desea: "))
    for i in range(len(li_precios)):
        if li_precios[i] < precio_usuario:
            print("nombre: ", li_nombres[i], " ", "precio: ", li_precios[i])


def menu():
    print("ingrese una de las opciones:")
    print("1- cargar nombres de los articulos y sus precios")
    print("2- imprimir nombres y precios.")
    print("3- imprimir el nombre del articulo mayor.")
    print("4- importe menor al valor ingresado por el usuario.")
    print("5- salir.")
#bloque principal
opc = 0
while opc != 5:
    menu()
    opc = int(input())
    if opc == 1:
        lista_nombres,lista_precios = cargar_listas()
    elif opc == 2:
            imprimir_nombres_precios(lista_nombres, lista_precios)    
    elif opc == 3:
        print("el precio de mayor articulo es: ", articulo_mayor_precio(lista_nombres, lista_precios))
    elif opc == 4:
            articulos_menores(lista_nombres, lista_precios)

