class Operaciones:

    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
    
    def cargar1(self):
        self.valor1 = int(input("ingrese el primer valor:"))
    
    def cargar2(self):
        self.valor2 = int(input("ingrese el segundo valor:"))
    
    def imprimir_resultado(self):
        print("el resultado es:", self.resultado)

class Sumar(Operaciones):

    def __init__(self):
        super().__init__()
        super().cargar1()
        super().cargar2()
    
    def operar(self):
        self.resultado = self.valor1 + self.valor2
    
    def mostrar_resultado(self):
        super().imprimir_resultado()

class restar(Operaciones):

    def __init__(self):
        super().__init__()
        super().cargar1()
        super().cargar2()
    
    def operar(self):
        self.resultado = self.valor1 - self.valor2
    
    def mostrar_resultado(self):
        print("la resta.")
        super().imprimir_resultado()

# bloque principal

sumar1 = Sumar()
sumar1.operar()
sumar1.mostrar_resultado()
resta1 = restar()
resta1.operar()
resta1.mostrar_resultado()
