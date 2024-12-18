class Persona:

    def __init__ (self):
        self.nombre = input("ingrese el nombre de la persona:")
        self.edad = int(input("ingrese la edad de la persona:"))
    
    def imprimir(self):
        print("el nombre es:",self.nombre, "tiene", self.edad,"de edad")
    
class Cliente(Persona):

    def __init__ (self):
        super().__init__()
        self.sueldo = float(input("ingrese el sueldo del cliente: "))
    
    def mostrar(self):
        super().imprimir()
        print("el sueldo de la persona es: ", self.sueldo)
    
    def mostrar_pagaImpuesto(self):
        if self.sueldo > 3000:
            print(self.nombre, "debe pagar impuestos")
        else:
            print(self.nombre, "no debe pagar impuestos")

# bloque principal

cliente1 = Cliente()
cliente1.mostrar()
cliente1.mostrar_pagaImpuesto()
        