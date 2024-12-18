class Operacion:

    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
    
    def carga1(self):
        self.valor1 = int(input("ingrese el primer valor:"))
    
    def carga2(self):
        self.valor2 = int(input("ingrese el segundo valor: "))
    
    def mostrar_resultado(self):
        print("el resultado es:",self.resultado)

class Sumar(Operacion):

    def operar(self):
        self.carga1()
        self.carga2()
        self.resultado = self.valor1 + self.valor2
    
class Restar(Operacion):

    def operar(self):
        self.carga1()
        self.carga2()
        self.resultado = self.valor1 - self.valor2

        
    
        

# bloque principal

suma1 = Sumar()
suma1.operar()
suma1.mostrar_resultado()
resta1 = Restar()
resta1.operar()
resta1.mostrar_resultado()