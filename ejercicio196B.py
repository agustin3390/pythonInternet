class Persona:

    def __init__(self):
        self.nombre = input("ingrese el nombre del empleado:")
        self.edad = int(input("ingrese la edad del empleado:"))
    
    def imprimir(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)

class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo = float(input("ingrese el sueldo:"))
    
    def separar(self):
        print("--------------------------")
    
    def mostrar_datos(self):
        print("Datos personales.")
        super().imprimir()
        print("sueldo:", self.sueldo)
    
    def paga_impuestos(self):
        if self.sueldo >= 3000:
            print(self.nombre, "debe pagar impuestos.")
        else:
            print(self.nombre, "no debe pagar impuestos.")

# bloque principal

empleado1 = Empleado()
empleado1.separar()
empleado1.mostrar_datos()
empleado1.separar()
empleado1.paga_impuestos()