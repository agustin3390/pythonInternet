def mensaje_saludo(mensaje):
    print("**********************************")
    print(mensaje)
    print("**********************************")

def suma():
    valorUno = int(input("ingrese el priemr valor: "))
    valorDos = int(input("ingrese el segundo valor: "))
    resultado = valorUno + valorDos
    print("el resultado es: ", resultado)
#bloque principal

mensaje = "bienvenidos al programa..."
mensaje_saludo(mensaje)
suma()
mensaje = "saludos. gracias por adherirse a nuestro programa..."
mensaje_saludo(mensaje)