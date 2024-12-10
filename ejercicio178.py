class Empleado:

    def __init__(self):
        self.nombre = input("ingrese el nombre del empleado: ")
        self.sueldo = float(input("ingrese el sueldo del empleado: "))
    
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("sueldo: ", self.sueldo)

    def imprimir_pagoImpuesto(self):
        if self.sueldo > 3000:
            print(self.nombre,"debe pagar impuestos")
        else:
            print(self.nombre, "no se debe pagar impuestos")


# bloque principal

empleado1 = Empleado()
empleado1.imprimir()
empleado1.imprimir_pagoImpuesto()