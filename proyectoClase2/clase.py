class Triangulo:

    def inicializacion(self):
        self.lado1 = int(input("ingrese el primer lado: "))
        self.lado2 = int(input("ingrese el segundo lado: "))
        self.lado3 = int(input("ingrese el tercer lado: "))

    def imprimir_mayor(self):
        print("el lado mayor es: ")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)
    
    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("el triangualo es equilatero.")
        else:
            print("el triangulo no es equilatero.")
    