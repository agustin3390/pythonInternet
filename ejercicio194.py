import random
class Dados:

    def __init__(self):
        self.dado = 1#random.randint(1,6)
    
    def retornar_valor(self):
        return self.dado
    
    def imprimir(self):
        print("el valor es:", self.dado)
    
class JuegoDeDados:

    def __init__(self):
        self.dado1 = Dados()
        self.dado2 = Dados()
        self.dado3 = Dados()
        

    
    def jugar(self):
        self.dado1.imprimir()
        self.dado2.imprimir()
        self.dado3.imprimir()
        if self.dado1.retornar_valor() == self.dado2.retornar_valor() and self.dado1.retornar_valor() == self.dado3.retornar_valor():
            print("gano el juego")
        else:
            print("perdio el juego")

# bloque principal
juegosdedados1 = JuegoDeDados()
juegosdedados1.jugar()

