class Operaciones:

    def __init__ (self):
        self.num1 = int(input("ingrese el primer numero: "))
        self.num2 = int(input("ingrese el segundo numero: "))
        self.suma()
        self.resta()
        self.multiplicar()
        self.division()
    
    def suma(self):
        suma = self.num1 + self.num2
        print("la suma es:", suma)
    
    def resta(self):
        resta = self.num1 - self.num2
        print("la resta es: ", resta)
    
    def multiplicar(self):
        producto = self.num1 * self.num2
        print("el producto es:", producto)
    
    def division(self):
        division = self.num1 / self.num2
        print("la division es:", division)