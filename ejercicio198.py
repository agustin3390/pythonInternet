class Cuenta:

    def __init__(self):
        self.titular = input("ingrese el nombre del titular:")
        self.monto = float(input("ingrese el monto:"))
    
    def imprimir(self):
        print("titular:",self.titular)
        print("monto:", self.monto)
    
class cajaAhorro(Cuenta):

    def __init__(self):
        super().__init__()
    
    def mostrar(self):
        print("cuenta Caja de Ahorro.")
        super().imprimir()

class PlazoFijo(Cuenta):

    def __init__(self,plazo,interes):
        super().__init__()
        self.plazo = plazo
        self.interes = interes
        self.ganancia_interes = 0
    
    def mostrar(self):
        print("Plazo Fijo.")
        super().imprimir()
        print("plazo:", self.plazo, "dias")
        print("interes:", self.interes)
        self.ganancias()
    
    def ganancias(self):
        self.ganancia_interes = self.monto * self.interes/100
        print("ganancias:", self.ganancia_interes)






# bloque principal

cajaAhorro1 = cajaAhorro()
cajaAhorro1.mostrar()
plazoFijo1 = PlazoFijo(30, 0.7)
plazoFijo1.mostrar()