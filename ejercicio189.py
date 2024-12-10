class Cuadrado:

    def __init__ (self, lado):
        self.lado = lado
        self.superficie()
        self.perimetro()
    
    def superficie(self):
        superficie = self.lado * self.lado
        print("la superficie es: ", superficie)
    
    def perimetro(self):
        perimetro = self.lado * 4
        print("perimetro es igual a: ", perimetro)
    
    